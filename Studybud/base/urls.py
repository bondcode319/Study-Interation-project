from django.urls import path
from . import views
from base.api import views as api_views

urlpatterns =[
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    
    
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"), 
    
    
    path('update-user/', views.updateUser, name="update-user"),
    
    
    path('topics/', views.topicPage, name="topics"), 
    path('activity/', views.activityPage, name="activity"),
    
    # API routes
    path('api/', api_views.getRoutes, name="api-routes"),
    path('api/rooms/', api_views.getRooms, name="api-rooms"),
    path('api/rooms/<str:pk>/', api_views.getRoom, name="api-room"),
]

