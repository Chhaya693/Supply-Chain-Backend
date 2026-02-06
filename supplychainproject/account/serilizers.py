from rest_framework import serializers
from account.models import MyUser

class Register(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    # Password2 = serializers.IntegerField()
    class Meta:
        model = MyUser
        fields = ["id", "name","email","password","password2"]

    
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password and confirm password do not match")
        return attrs
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')

        user = MyUser(**validated_data)
        user.set_password(password)   # <-- VERY IMPORTANT
        user.save()
        return user
    

class Login(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = MyUser
        fields = ["email","password"]