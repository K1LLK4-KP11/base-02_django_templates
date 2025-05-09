from django.urls import path
from posts import views 

urlpatterns = [
    path('PostList/', views.post_list, name='post list'),
]