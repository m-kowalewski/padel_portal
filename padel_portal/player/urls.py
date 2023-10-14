from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    # path('player_create', views.PlayerCreate.as_view(), name="player_create"),
    path('home', views.PlayerList.as_view(), name="home"),
    path('sign_up', views.PlayerCreate.as_view(), name="player_create"),
    path('player_update/<int:pk>', views.PlayerUpdate.as_view(), name="player_update"),
    path('player_list', views.PlayerList.as_view(), name="player_list"),
]