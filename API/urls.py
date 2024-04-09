from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from mother.models import *

urlpatterns =[
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getMoms),
    path('/addmom/',views.addMom),
    path('/getchilds/',views.childProfile),
    path('/addchild/',views.addChild),
    path('/getchild/<str:pk>/',views.getchild),
    path('/updatechilds/<str:pk>/',views.updateChild),
    path('/getTeacher/',views.getTeacher),
    path('/deletechild/<str:pk>/',views.deleteChild),
    path('/readreport/<str:pk>/',views.readReport),
    path('/createreport/',views.createReport),
]

    