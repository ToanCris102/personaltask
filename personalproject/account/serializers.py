from asyncore import write
from pyexpat import model
from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={
            'input_type': 'password',
            'placeholder': "Password",
        }
    )
    
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            # 'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )              
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class MyTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD
    def validate(self, attrs):
        user = User.objects.filter(email=attrs[self.username_field]).first()
        username = user.username
        print(user)
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
        print(data)
        self.user = authenticate(**data)
        refresh = self.get_token(self.user)
        
        data = {
            "refresh": str(refresh),
            "access" : str(refresh.access_token)
        }
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'
    