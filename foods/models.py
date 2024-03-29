from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=200)
  category = models.CharField(max_length=30, blank=True)

  energy = models.FloatField(default=0.0)
  protein = models.FloatField(default=0.0)
  fat = models.FloatField(default=0.0)
  carbohydrate = models.FloatField(default=0.0)
  
  dietary_fiber = models.FloatField(default=0.0)
  magnesium = models.FloatField(default=0.0)
  vitamin_a = models.FloatField(default=0.0)
  vitamin_d = models.FloatField(default=0.0)
  vitamin_b6 = models.FloatField(default=0.0)
  folic_acid = models.FloatField(default=0.0)
  vitamin_b12 = models.FloatField(default=0.0)
  tryptophan = models.FloatField(default=0.0)
  dha_epa = models.FloatField(default=0.0)

  classifier = models.IntegerField(default=0)
  lang = models.CharField(max_length=30, default='ko') # 임시 추가

  def __str__(self):
    return f'[{self.id}]{self.name} :: {self.category}'

# just for English Version(Landing Page)
class Efood(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=30, blank=True)

  energy = models.FloatField(default=0.0)
  protein = models.FloatField(default=0.0)
  fat = models.FloatField(default=0.0)
  carbohydrate = models.FloatField(default=0.0)
  
  dietary_fiber = models.FloatField(default=0.0)
  magnesium = models.FloatField(default=0.0)
  vitamin_a = models.FloatField(default=0.0)
  vitamin_d = models.FloatField(default=0.0)
  vitamin_b6 = models.FloatField(default=0.0)
  folic_acid = models.FloatField(default=0.0)
  vitamin_b12 = models.FloatField(default=0.0)
  tryptophan = models.FloatField(default=0.0)
  dha_epa = models.FloatField(default=0.0)

  classifier = models.IntegerField(default=0)

  def __str__(self):
    return f'[{self.id}]{self.name} :: {self.category}'


# class Ename(models.Model):
#   name = models.CharField(max_length=255)
#   food_info = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True, blank=True)
#   classifier = models.IntegerField(default=0)

class Supplement(models.Model):
  name = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  # 13개 영양소 필드 추가
  energy = models.FloatField(default=0.0)
  protein = models.FloatField(default=0.0)
  fat = models.FloatField(default=0.0)
  carbohydrate = models.FloatField(default=0.0)
  
  dietary_fiber = models.FloatField(default=0.0)
  magnesium = models.FloatField(default=0.0)
  vitamin_a = models.FloatField(default=0.0)
  vitamin_d = models.FloatField(default=0.0)
  vitamin_b6 = models.FloatField(default=0.0)
  folic_acid = models.FloatField(default=0.0)
  vitamin_b12 = models.FloatField(default=0.0)
  tryptophan = models.FloatField(default=0.0)
  dha_epa = models.FloatField(default=0.0)

  def __str__(self):
    return f'[{self.id}]{self.name} :: {self.manufacturer}'