from django.urls import path
import api.views as views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('posts/new', views.create_post, name='post_new'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
]
