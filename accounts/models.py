from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  GENDER_CHOICES = (
    ('M', 'M'),
    ('F', 'F'),
  )
  username = models.CharField(max_length=15, unique=True, blank=True)
  # 성별 나이 추가
  gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default='M', null=True) # before - false , null필드 없음
  age = models.PositiveIntegerField(default=0) # before - false, null 필드 없음

  def __str__(self):
    return self.username