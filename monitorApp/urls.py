from django.urls import path
from . import views

urlpatterns = [
path('', views.monitorApp, name="app"),
path('dashboard',  views.monitorApp, name="dashboard"),
path('inference/', views.video_feed, name="inference"),
path('analysis/', views.analysis, name="analysis"),
]
