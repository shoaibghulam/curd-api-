from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register',UserRegisterView.as_view()),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('curd', Curd.as_view(), name='about'),
    path('curd/<int:id>', Curd.as_view(), name='about'),
    path('curd-view/<int:id>', CurdSingle.as_view(), name='singlepost')
  
]
