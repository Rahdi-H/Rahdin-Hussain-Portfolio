from django.urls import path
from . import views

urlpatterns = [
    path('', views.skills, name='skills'),
    path('django/', views.django, name='django'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('tailwindcss/', views.tailwindcss, name='tailwindcss'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('update/<int:id>/', views.update_data, name='update'),
]