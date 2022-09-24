from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
from foods.models import Food, Supplement

# BASE
class BasePost(models.Model):
  TYPE_CHOICES = (
    ('breakfast', '아침'),
    ('lunch', '점심'),
    ('dinner', '저녁'),
    ('snack', '간식'),
    ('supplement', '영양제'),
    ('water', '물'),
  )
  type = models.CharField(max_length=12, choices=TYPE_CHOICES, default=' ')
  created_at = models.DateTimeField(blank=True, null=True) # datetimefield 사용해야 범위로 가져올 수 있음!
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

# FOOD
class FoodPost(BasePost):
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f'[{self.pk}]{self.created_at}||{self.author}\'s {self.type}' # 이래도 나중에 성능 괜찮을까..??
    # return f'[{self.pk}]{str(self.created_at)[:10]}|{self.author}\'s {self.type}' # 이래도 나중에 성능 괜찮을까..??

class FoodImage(models.Model):
  post = models.ForeignKey(FoodPost, on_delete=models.CASCADE, null=True, blank=True)
  image = models.CharField(max_length=250, blank=True)
  def __str__(self):
    return f'<{self.pk}>[post_no.{self.post.id}]{self.image}'
    # return f'[post_no.{self.post}]{self.image}'

class FoodConsumption(models.Model):
  post = models.ForeignKey(FoodPost, on_delete=models.CASCADE, null=True, blank=True)
  food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
  amount = models.IntegerField(default=0)
  def __str__(self):
    return f'<{self.pk}>[post_no.{self.post.id}]{self.food.name}, {self.amount}'

# SUPPLEMENT
# class SupplementPost(BasePost):
#   author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#   def __str__(self):
#     return f'[{self.pk}] {self.author}\'s post :: {self.created_at}'

class SupplementPost(BasePost):
  # post = models.ForeignKey(SupplementPost, on_delete=models.CASCADE, null=True, blank=True)
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  supplement = models.ForeignKey(Supplement, on_delete=models.SET_NULL, blank=True, null=True, default=1) # 나중에 DB에 인스턴스 생성 후 연결
  name = models.CharField(max_length=100, default='')
  manufacturer = models.CharField(max_length=100, default='')
  # amount = models.IntegerField(default=0) # 필요없을 듯
  image = models.CharField(max_length=250, blank=True)  # S3 주소 저장

  def __str__(self):
    return f'[{self.pk}] {self.author}\'s post :: {self.created_at}'


# WATER
class WaterPost(BasePost):
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  amount = models.IntegerField(default=0)

  def __str__(self):
    return f'[{self.pk}]{self.author}\'s post :: {self.amount} ({self.created_at})'

  

'''
class FoodConsumption(models.Model):
  MEAL_CHOICES = (
    ('breakfast', '아침'),
    ('lunch', '점심'),
    ('dinner', '저녁'),
    ('snack', '간식'),
  )

  # fk 미사용
  # post = models.IntegerField(default=0) # food.id를 int로 저장
  food = models.IntegerField(default=0) # food.id를 int로 저장
  # fk 사용
  # post = models.ForeignKey(Post, on_delete=models.CASCADE)
  # food = models.ForeignKey(Food, on_delete=models.CASCADE)
  amount = models.IntegerField(default=0) # g 또는 ml
  meal_type = models.CharField(max_length=12, choices=MEAL_CHOICES, default=' ')
  # fk 미사용
  author = models.IntegerField(default=0) # user.id를 int로 저장
  # fk 사용 
  # author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  created_at = models.DateTimeField(blank=True) # datetimefield 사용해야 범위로 가져올 수 있음!
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return f'<{self.id}>[user_no.{self.author}]{self.created_at}|{self.food}|{self.amount}|{self.meal_type}'

class FoodImage(models.Model):
  MEAL_CHOICES = (
    ('breakfast', '아침'),
    ('lunch', '점심'),
    ('dinner', '저녁'),
    ('snack', '간식'),
  )
  # fk 미사용
  # post = models.IntegerField(default=0)
  # fk 사용
  # post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.IntegerField(default=0) # user.id를 int로 저장
  image = models.CharField(max_length=250, blank=True)
  meal_type = models.CharField(max_length=12, choices=MEAL_CHOICES, default=' ')
  created_at = models.DateTimeField(blank=True) # datetimefield 사용해야 범위로 가져올 수 있음!
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'<{self.id}>[user_no.{self.author}]{self.image}'
'''