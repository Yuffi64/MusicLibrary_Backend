from django.urls import path
from . import views #LikeView

urlpatterns = [
    path('', views.music_list),
    path('<int:pk>/', views.music_detail),
#    path('like/<int:pk>', LikeView, name='like_song'),
]