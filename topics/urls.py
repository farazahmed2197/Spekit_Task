from django.urls import path
from topics import views

urlpatterns = [
    path('', views.TopicList.as_view()),
    path('object_topics/', views.TopicsOfObject.as_view()),
    path('<int:pk>/', views.TopicDetail.as_view()),
]