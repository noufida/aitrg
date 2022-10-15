
from django.urls import path
from . import views
# simple jwt token specifications
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('register/',views.admin_register,name='admin_register'),
    #  for admin login with token 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    
    # for refresh token setup
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]