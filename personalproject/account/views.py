from django.shortcuts import render, get_object_or_404
from rest_framework_simplejwt import tokens
from rest_framework import generics, response, status, permissions, response, exceptions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from . import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
User = get_user_model()
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime
from . import utils
from . import models
# @access Public 
# @method POST
# @desc For regist account
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        
        self.user = serializer.save()        
        
    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        refresh = tokens.RefreshToken.for_user(self.user)
        data_response = data.data
        data_response["refresh"] = str(refresh)
        data_response["access"] = str(refresh.access_token)      
        
        return response.Response(data=data_response, status=status.HTTP_201_CREATED)

# @access Public 
# @method POST
# @desc For User login
class MyTokenObtainPairView(TokenObtainPairView):    
    serializer_class = serializers.MyTokenObtainSerializer
    permission_classes = [permissions.AllowAny]
# class ForgotPasswordView(generics.CreateAPIView):    
#     # queryset = User.objects.filter()
#     serializer_class = serizlizers.ForgotPasswordSerializer
#     permission_classes = [permissions.AllowAny]
#     def get_queryset(self) :
#         user = self.request.user
#         print(user.email)
#         print(User.objects.filter(email=user.email))
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
        
#         serializer.is_valid(raise_exception=False)   
#         return serializer.validated_data['email']
#         # print(serializer.validated_data['email'])    
#         # print(serializer.data)
#         # return response.Response(serializer.data, status=status.HTTP_201_CREATED)

# @access Public 
# @method POST
# @desc Send token and URL fronend to user' mail 
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def ForgotPassword(request):
    try: 
        url = request.data['url']
        email = request.data['email']
        user = User.objects.get(email=email)
        day = datetime.now()
        subject = "Token for reset password: " + str(day)
        refresh = tokens.RefreshToken.for_user(user) 
        token    = str(refresh.access_token)
        to      = email  
        msg_res = utils.my_mail(subject, token, url , to)
        
        res = {
            'message': msg_res,
            # 'access': str(refresh.access_token),
        }
        return response.Response(data=res, status=status.HTTP_200_OK)
    except:
        res_err = {
            'message': "Data error or email don't exist!!!",
        }
        return response.Response(data=res_err, status=status.HTTP_404_NOT_FOUND)
    
    
# @access Private: Users with their' token
# @method PUT
# @desc For users Change password when They forgot password
class ChangePasswordWithTokenView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordWithToken
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, queryset=None):
            obj = self.request.user
            return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            
            self.object.save()
            refresh = tokens.RefreshToken.for_user(self.object)
            
            res = {
                'message': 'Password updated successfully',
                'token': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }

            return response.Response(data=res, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# @access Private: Users with their' token
# @method PUT
# @desc For users change password
class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = serializers.ChangePasswordSerializer
        # model = User
        permission_classes = [permissions.AllowAny, permissions.IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return response.Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                
                self.object.save()
                refresh = tokens.RefreshToken.for_user(self.object)
                
                res = {
                    'message': 'Password updated successfully',
                    'token': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    }
                }

                return response.Response(data=res, status=status.HTTP_200_OK)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @access Private: Users with their' token
# @method PUT
# @desc For users change password
# class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     # queryset = models.Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = None
#     def get_queryset(self):
#         queryset = models.Profile.objects.get(auth_id=self.request.user.id)
#         return queryset
    
    # def update(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(data=request.data)
    
    # def update(self, request, *args, **kwargs):
    #         self.object = self.get_object()
    #         serializer = self.get_serializer(data=request.data)

    #         if serializer.is_valid():
    #             # Check old password
    #             if not self.object.check_password(serializer.data.get("old_password")):
    #                 return response.Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
    #             # set_password also hashes the password that the user will get
    #             self.object.set_password(serializer.data.get("new_password"))
                
    #             self.object.save()
    #             refresh = tokens.RefreshToken.for_user(self.object)
                
    #             res = {
    #                 'message': 'Password updated successfully',
    #                 'token': {
    #                     'access': str(refresh.access_token),
    #                     'refresh': str(refresh),
    #                 }
    #             }

    #             return response.Response(data=res, status=status.HTTP_200_OK)

    #         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = serializers.ProfileWriteSerializer
    # queryset = models.Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = get_object_or_404(models.Profile,auth_id=self.request.user)
        return queryset
    def get_object(self, queryset=None):
        obj = get_object_or_404(models.Profile,auth_id=self.request.user)
        # obj = models.Profile.objects.get(auth_id=self.request.user)
        return obj
    
    
    
class UpdateAndDetailProfileView(generics.RetrieveUpdateAPIView):
    # serializer_class = serializers.UserUpdateSerializer
    def get_object(self, queryset=None):
        if self.request.method == 'GET':
            obj = get_object_or_404(models.Profile,auth_id=self.request.user)
        elif self.request.method == 'PUT' or self.request.method == 'PATCH': 
            obj = User.objects.get(id=self.request.user.id)
        return obj
    
    def get_serializer_class(self):        
        if self.request.method == 'GET':
            self.serializer_class =  serializers.ProfileReadSerializer 
        else:
            self.serializer_class = serializers.UserUpdateSerializer
        return super().get_serializer_class()