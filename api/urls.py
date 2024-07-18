from django.urls import path
import api.views as views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.create_user, name='user_new'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/new/', views.create_post, name='post_new'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
]
