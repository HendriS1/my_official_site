from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name="events"),
    path('create_user', views.create_user, name='create_user'),
    path('user_login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
         name='authenticate_user'),
    path('show_user/', views.show_user,
         name='show_user'),
    path('logout_user', views.logout_user, name="logout")
]
