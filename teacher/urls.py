from django.urls import path
from teacher import views

urlpatterns = [
    path('teachers',views.teachers,name='teachers'),
    path('teacherRegisteration',views.teacherRegisteration,name='teacherregister'),
    path('loginTeacher',views.loginTeacher,name='loginteacher'),
    path('chileprofile/<str:pk>/',views.childprofile,name='childprofile'),
    path('logoutUser',views.logoutUser,name='logoutuser'),
    path('createReport/<str:pk>/',views.createReport,name='createreport'),
    path('readreport/<str:pk>/',views.readReport,name='readreport')
]