from django.urls import path
from cd import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('create_disk/', views.create_disk),
    path('edit/<int:id>/', views.edit),
    path('edit_lib/<int:id>/', views.edit_lib),
    path('delete/<int:id>/', views.delete),
    path('delete_lib/<int:id>/', views.delete_lib),
]
