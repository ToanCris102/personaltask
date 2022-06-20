from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='regist'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', views.TokenRefreshView.as_view(), name='refresh_token'),
    path('forgot-password/', views.ForgotPassword, name='forgot_password'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password')
]