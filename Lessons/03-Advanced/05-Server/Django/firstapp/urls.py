from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.user_view, name='users_view'),
    path('users/details/<int:id>', views.detailed_user_view, name='user_detailed_view'),
]