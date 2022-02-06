from django.urls import path
from topics import views

urlpatterns = [
    path('', views.FolderList.as_view()),
    path('topic_folders/', views.TopicFolderList.as_view()),
    path('all_topics/', views.AllTopicsOfFolder.as_view()),
    path('<int:pk>/', views.FolderDetail.as_view()),
]