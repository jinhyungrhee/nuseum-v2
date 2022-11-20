from django.urls import path
from . import views

urlpatterns = [
  # 식단일기
  # food
  path('food/', views.FoodPostCreateAPIView.as_view()), # 식단일기 음식 탭 저장(POST) api
  path('food/<int:pk>/', views.FoodConsumptionUpdateAPIView.as_view()), # FoodConsumption update(PATCH), delete
  path('food/image/<int:pk>/', views.FoodImageDeleteAPIView.as_view()), # FoodImage delete
  # path('food/view/', views.FoodTypeListAPIView.as_view()), # 식단일기 음식 탭 별로 저장된 것들 가져오는(GET) api (query param : type, date) -> deprecated
  # supplement
  path('supplement/', views.SupplementCreateAPIView.as_view()), # 영양제 생성(POST) -> deprecated ?
  path('supplement/<int:pk>/', views.SupplementUpdateAPIView.as_view()), # 영양제 수정(PATCH), 삭제(DELETE)
  path('supplement/post/', views.SupplementCreateDBAPIView.as_view()), # new 영양제 생성(POST) api
  # water
  path('water/', views.WaterCreateAPIView.as_view()), # 물 생성(POST)
  path('water/<int:pk>/', views.WaterUpdateAPIView.as_view()), # 물 수정(PATCH)
  # today
  path('today/', views.TodayView.as_view()), # 오늘 탭(GET)
  # 식이분석
  # day
  path('day/', views.DayNutrientView.as_view()),
  # week
  path('week/', views.WeekNutrientView.as_view()),
  # month
  path('month/', views.MonthNutrientView.as_view()),
  # admin - 유저리스트
  path('admin/', views.AdminView.as_view()),
  # admin - 구간별 음식 합계
  path('admin/sum/', views.AdminSumView.as_view()),
  # admin - 식이분석(쿼리파라미터 : 유저명, 날짜)
  path('admin/analysis/day/', views.AdminDayView().as_view()),
  path('admin/analysis/week/', views.AdminWeekView().as_view()),
  path('admin/analysis/month/', views.AdminMonthView().as_view()),
  # TODO : admin - 사용자별 식단 추가 입력
  path('admin/addition/', views.AdminPostCreateView().as_view()),
]
