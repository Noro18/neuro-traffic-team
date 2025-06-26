
from django.contrib import admin
from django.urls import path, include
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls, name="admins"),
    path('admin/', staff_member_required(admin.site.index), name="admin"),
    path('', include('monitorApp.urls'))
]
