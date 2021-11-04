from django.urls import path
from lab4 import views

urlpatterns = [
    path('', views.menu),
    path('page/<int:id>/', views.page, name='page_url'),
]
