from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from dj_rest_auth.serializers import JWTSerializer
from django.conf import settings
from django.utils.module_loading import import_string
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):

  def validate_username(self, username):
        codes = ['사과', '오이', '호박', '당근' , '시금치', '열무' , '토란', '감자', '브로콜리', '양배추', '비트', '테스트1', '테스트2', '테스트3', '테스트4', '테스트5'] # 30명 코드
        username = get_adapter().clean_username(username)
        if username not in codes:
          raise serializers.ValidationError(_("올바른 코드를 입력하세요!"))
        return username

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'is_superuser']

class UserListSerializer(serializers.Serializer):
  userList = UserSerializer(many=True)

# 로그인 response 처리
# Get the UserModel
UserModel = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            # We don't need to call the all-auth
            # username validator unless its installed
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'is_superuser'): # 추가
            extra_fields.append('is_superuser')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)


class CustomJWTSerializer(JWTSerializer):
  """
  Serializer for JWT authentication.
  """
  access_token = serializers.CharField()
  refresh_token = serializers.CharField()
  user = serializers.SerializerMethodField()

  def get_user(self, obj):
      """
      Required to allow using custom USER_DETAILS_SERIALIZER in
      JWTSerializer. Defining it here to avoid circular imports
      """
      rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

      JWTUserDetailsSerializer = import_string(
          rest_auth_serializers.get(
              'USER_DETAILS_SERIALIZER',
              # 'dj_rest_auth.serializers.UserDetailsSerializer',
              'accounts.serializers.UserDetailsSerializer',
          ),
      )

      user_data = JWTUserDetailsSerializer(obj['user'], context=self.context).data
      return user_data