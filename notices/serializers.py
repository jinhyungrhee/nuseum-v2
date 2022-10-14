from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notice
    fields = '__all__'
    # exclude = ('user_list',)

  def create(self, validated_data):
    notice = Notice.objects.create(**validated_data)
    return notice

class CustomNoticeSerializer(serializers.Serializer):
  id = serializers.CharField()
  clicked = serializers.IntegerField()