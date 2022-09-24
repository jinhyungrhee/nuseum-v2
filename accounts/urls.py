from django.urls import path, include
from .views import *
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)

urlpatterns = [
  # path('', include('dj_rest_auth.urls')),
  # URLs that do not require a session or valid token
  path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
  path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
  # path('login/', LoginView.as_view(), name='rest_login'),
  # test
  path('login/', CustomLoginView.as_view(), name='rest_login'),
  # URLs that require a user to be logged in with a valid session / token.
  path('logout/', LogoutView.as_view(), name='rest_logout'),
  path('user/', UserDetailsView.as_view(), name='rest_user_details'),
  path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
  # 회원가입
  path('registration/', include('dj_rest_auth.registration.urls')),
]