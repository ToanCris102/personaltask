from asyncore import read
from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={
            'input_type': 'password',
            'placeholder': "Password",
        }
    )    
    full_name = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name']
        extra_kwargs = {
            'email': {'write_only': True},
        }
    def create(self, validated_data):
        # print(validated_data['full_name'])
        # first_name=str(validated_data['full_name']).split(" ",1)[0]
        # last_name=str(validated_data['full_name']).split(" ",1)[1]
        # print(first_name, last_name)
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=str(validated_data['full_name']).split(" ",1)[0],
            last_name=str(validated_data['full_name']).split(" ",1)[1],
        )              
        
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(
            auth_id=user
        )

        return user
    
class MyTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD
    def validate(self, attrs):
        user = User.objects.filter(email=attrs[self.username_field]).first()
        username = user.username
        # print(user)
        if not user:
            raise exceptions.ValidationError('The user is not valid.')

        if user:
            if not user.check_password(attrs['password']):
                raise exceptions.ValidationError('Incorrect credentials.')
        
        
        # # if self.user is None or not self.user.is_active:
        # #     raise ValidationError('No active account found with the given credentials')
        
        data = {
            "username": user.username,
            "password": attrs["password"],
        }
        try:
            data["request"] = self.context["request"]
        except KeyError:
            pass
        # print(data)
        self.user = authenticate(**data)
        refresh = self.get_token(self.user)
        
        data = {
            "refresh": str(refresh),
            "access" : str(refresh.access_token)
        }
        return data
    

        
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['old_password', 'new_password']
        extra_kwargs = {
            'old_password': {'write_only':True},
            'new_password': {'write_only':True},
        }
        
class ChangePasswordWithToken(serializers.ModelSerializer):
    new_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['new_password']
        extra_kwargs = {
            'new_password': {'write_only':True},
        }

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name']

class ProfileReadSerializer(serializers.ModelSerializer): 
    auth_id = UserReadSerializer(read_only=True)
    theme_id = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = ['auth_id', 'theme_id']
        
        
class ProfileWriteSerializer(serializers.ModelSerializer):
    # auth_id = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ['theme_id',]
        extra_kwagrs = {
            # 'url': {"write_only":True},
            'theme_id': {"write_only":True},            
        }
    
    
    # def update(self, instance, validated_data):
    #     user_data = validated_data['auth_id']
    #     print(user_data)
    #     # game_data = validated_data.pop('games')
    #     username = self.data['auth_id']['username']
    #     user = User.objects.get(username=username)
    #     print(user)
    #     user_serializer = UserSerializer(data=user_data)
    #     if user_serializer.is_valid():
    #         user_serializer.update(user, user_data)
    #     instance.save()
    #     return instance
    
class UserUpdateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields= ['email', 'full_name']        
    
        extra_kwargs = {
            "email": {"write_only": True}
        }
    def save(self, **kwargs):
        kwargs['first_name'] = str(self.validated_data['full_name']).split(" ",1)[0]
        kwargs['last_name'] = str(self.validated_data['full_name']).split(" ",1)[1]
        return super().save(**kwargs)
        
    