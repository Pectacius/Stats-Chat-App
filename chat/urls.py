from django.urls import path

from . import views

urlpatterns = [
    # authentication paths
    path('', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('signup/', views.sign_up, name='sign_up'),

    path('index/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]
