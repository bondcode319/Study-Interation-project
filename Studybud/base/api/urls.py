from django.urls import path
from . import views 


urlpatterns =[
    path('', views.getRoutes),
    path('rooms/', views.getRooms),  # Changed to getRooms
    path('rooms/<str:pk>/', views.getRoom),
]
