from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('', views.monitorApp, name="app"),
path('dashboard',  login_required(views.dashboard), name="dashboard"),
path('inference/', login_required(views.video_feed), name="inference"),
path('analysis/', login_required(views.analysis), name="analysis"),
]
