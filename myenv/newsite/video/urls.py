from django.urls import path
from . import views

urlpatterns = [
	path('gettext/', views.video, name='video')   #для основного запроса
]
