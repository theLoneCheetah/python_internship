from django.urls import path
from . import views

urlpatterns = [
	path('video/', views.empty, name='empty'),   #для пустого запроса
	path('video/<str:text>/', views.video, name='video')   #для основного запроса
]
