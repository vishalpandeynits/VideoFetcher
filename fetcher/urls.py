from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.VideoListAPI.as_view(), name = "video_list_api")
]
