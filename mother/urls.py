from django.urls import path
from mother import views
urlpatterns = [
    path('mother',views.mothers,name='mother'),
    path('createChild/<str:pk>/', views.createChild, name='createchild'),
    path('register',views.registerUser,name='register'),
    path('',views.loginUser,name='login'),
    path('logoutUser/',views.logoutUser,name='logout'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('updateChild/<str:pk>/',views.updateChild,name='updatechild'),
    path('deleteChild/<str:pk>/',views.deleteChild,name='deletechild')
]