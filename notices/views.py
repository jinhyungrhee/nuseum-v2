from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notice
from .serializers import NoticeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class NoticeAPIView(APIView):

  def get(self, request):
    user = self.request.user.username
    isread = -1

    notices = Notice.objects.all().values()
    print(notices)

    for i in range(len(notices)):
      if f'{user}' in notices[i]['user_list']:
        isread = 1
      else:
        isread = 0

      # setattr(notices[i], str(user), isread)
      notices[i][str(user)] = isread
      # print(notices[i].NPP01)
    
    serializer = NoticeSerializer(instance=notices, many=True)

    # return Response(data=notices)
    return Response(data=serializer.data)

  def post(self, request):
    if not request.user.is_authenticated:
      return Response(status=status.HTTP_401_UNAUTHORIZED)
    # print(request.data)
    serializer = NoticeSerializer(data=request.data)
    print(dir(serializer))
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)