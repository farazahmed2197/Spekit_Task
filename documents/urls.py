from django.urls import path
from documents import views

urlpatterns = [
    path('', views.DocumentList.as_view()),
    path('topic_documents/', views.TopicDocumentList.as_view()),
    path('<int:pk>/', views.DocumentDetail.as_view()),
]