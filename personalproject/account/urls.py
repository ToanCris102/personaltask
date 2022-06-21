from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='regist'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('refresh-token/', views.TokenRefreshView.as_view(), name='refresh_token'),
    path('forgot-password/', views.ForgotPassword, name='forgot_password'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('change-password-with-token/', views.ChangePasswordWithTokenView.as_view(), name='change_password_with_token'),
]