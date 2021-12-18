from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideoList.as_view(), name = "video_list"),
    path('api/', views.VideoListAPI.as_view(), name = "video_list_api"),
    path('dashboard/', views.VideoListGenericAPI.as_view(), name = "dashboard")
]
