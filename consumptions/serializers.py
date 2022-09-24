from rest_framework import serializers
from .models import FoodPost, FoodConsumption, FoodImage, SupplementPost, WaterPost
from django.conf import settings
import base64
import boto3


# Food Serializers

class FoodPostImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodImage
    # fields = ['image']
    fields = '__all__'

  def create(self, validated_data):
    pass

class FoodConsumptionSerializer(serializers.ModelSerializer):
  name = serializers.ReadOnlyField(source='food.name')
  class Meta:
    model = FoodConsumption
    fields = '__all__'

class FoodPostSerializer(serializers.ModelSerializer):
  images = FoodPostImageSerializer(many=True)
  consumptions = FoodConsumptionSerializer(many=True)

  class Meta:
    model = FoodPost
    fields = ['id', 'type', 'created_at', 'updated_at', 'author', 'images', 'consumptions']

  def create(self, validated_data):
    images_data = validated_data.pop('images')
    foods_data = validated_data.pop('consumptions')
    post = FoodPost.objects.create(**validated_data)
    # print(f"IMG_DATA : {images_data}")
    # print(f"IMG_DATA_LIST : {list(images_data)}")
    # print(f"FOOD_DATA : {foods_data}")
    image_list = []
    food_list = []

    for image_data in images_data:
      food_image = FoodImage.objects.create(**image_data)
      food_image.post = post
      food_image.save()
      image_list.append(food_image)
    for food_data in foods_data:
      food_consumption = FoodConsumption.objects.create(**food_data)
      food_consumption.post = post
      food_consumption.save()
      food_list.append(food_consumption)

    # print(f"IMG_LIST: {image_list}")
    # print(f"FOOD_LIST: {food_list}")

    food_post = {
      'id' : post.id,
      'type' : post.type,
      'created_at' : post.created_at,
      'updated_at' : post.updated_at,
      'author' : post.author,
      'images' : image_list,
      'consumptions' : food_list
    }
    return food_post # 여기서 에러나는듯 -> serializer 형식에 맞게 만들어서 보내줘야 할듯!!!

# Supplement Seriaizers
class SupplementSerializer(serializers.ModelSerializer):
  class Meta:
    model = SupplementPost
    fields = '__all__' # edit시 프론트에서 image 필드는 입력받지 않도록 제한 필요! 

# Water Serializers
class WaterSerializer(serializers.ModelSerializer):
  class Meta:
    model = WaterPost
    fields = '__all__'

# Admin
class FoodAdminConsumptionSerializer(serializers.ModelSerializer):
  date = serializers.ReadOnlyField(source='post.created_at')
  name = serializers.ReadOnlyField(source='food.name')
  class Meta:
    model = FoodConsumption
    fields = '__all__'

class FoodAdminImageSerializer(serializers.ModelSerializer):
  date = serializers.ReadOnlyField(source='post.created_at')
  class Meta:
    model = FoodImage
    # fields = ['image']
    fields = '__all__'


# CREATE 이미지 처리
class ImageDecodeSerializer(serializers.ModelSerializer):

  class Meta:
    model = FoodImage
    fields = '__all__'

  def create(self, validated_data):
    print(f"VALIDATED_DATE : {validated_data}")
    print(f"SELF.CONTEXT : {self.context}")
    post = self.context.get("post")
    meal_type = self.context.get("meal_type")
    date_data = self.context.get("date")
    image_id = self.context.get("image_id")


    year = date_data.strftime('%Y')
    month = date_data.strftime('%m')
    day = date_data.strftime('%d')
    # print("context.get(\"images\") LOG:", self.context.get("images")) 
    image_string = self.context.get("image_string") # String으로 들어옴! -> 시간 단축!
    header, data = image_string.split(';base64,')
    # header, data = image_string[num].split(';base64,') # 리스트째로 들어옴!
    data_format, ext = header.split('/')
    try:
      # food = FoodImage.objects.create(post=post, image='', meal_type=meal_type) # 이미지 객체 생성하여 DB에 임시 저장(url은 빈 string) *
      food_image = FoodImage.objects.get(id=image_id)
      image_data = base64.b64decode(data) # 이미지 파일 생성
      s3r = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
      key = "%s"%(f'{year}/{month}/{day}')
      s3r.Bucket(settings.AWS_STORAGE_BUCKET_NAME).put_object(Key=key+'/%s'%(f'{post}_{meal_type}_{food_image.id}.{ext}'), Body=image_data, ContentType='jpg')
      aws_url = f'{settings.IMAGE_URL}/{year}/{month}/{day}/{post}_{meal_type}_{food_image.id}.{ext}'
      # FoodImage.objects.update(post=post, image=aws_url, meal_type=meal_type, partial=True) # 이미지 객체 생성하여 DB에 저장
      food_image.image = aws_url # 위에서 생성된 food객체의 image_url 업데이트 *
      food_image.save()
    except TypeError:
      self.fail('invalid_image')
      
    return food_image