from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('user_info/', views.user_info, name='user_info'),
]


