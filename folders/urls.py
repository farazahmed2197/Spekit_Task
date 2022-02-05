from django.urls import path
from folders import views

urlpatterns = [
    path('folders/', views.folder_list),
    path('folders/<int:pk>/', views.folder_detail),
]