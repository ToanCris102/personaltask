from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='regist'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', views.TokenRefreshView.as_view(), name='refresh_token'),
    path('forgot-password/', views.ForgotPasswordView, name='forgot_password')
]