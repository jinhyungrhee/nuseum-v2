from django.db import models

# Create your models here.
class Notice(models.Model):
  content = models.TextField()
  user_list = models.TextField(default='', null=True, blank=True)
  
  def __str__(self):
    return f'[{self.id}] {self.content}'
