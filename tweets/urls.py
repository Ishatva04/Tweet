from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('create/', views.create_tweet, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='tweet_delete'),
    path('register/', views.register, name='register')
]