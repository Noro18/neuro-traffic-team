from django.urls import path
from . import views

urlpatterns = [
    path('', views.monitorApp, name="app"),
    path('inference/', views.video_feed, name = "inference")
]
