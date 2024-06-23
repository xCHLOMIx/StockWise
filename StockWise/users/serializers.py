from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phonenumber', 'password']
    
    def validate(self, attrs):
        phonenumber_exists = User.objects.filter(email = attrs['phonenumber']).exists()
        if phonenumber_exists:
            raise ValidationError("The Email has already been used!")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)

        user.save()

        Token.objects.create(user = user)

        return user