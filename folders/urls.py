from django.urls import path
from folders import views

urlpatterns = [
    path('', views.FolderList.as_view()),
    path('topic_folders/', views.TopicFolderList.as_view()),
    path('<int:pk>/', views.FolderDetail.as_view()),
]