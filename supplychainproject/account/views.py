from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import MyUser
from account.serilizers import Register,Login
from django.contrib.auth import authenticate
from rest_framework import status


class RegisterAPI(APIView):
    def get(self,request, format=None):
        mode= MyUser.objects.all()
        serilizer = Register(mode,many=True)
        return Response (serilizer.data)
    
    def post(self,request,format=None):
        serilizer = Register(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response("Register sucessfully",)
        return Response(serilizer.errors)
    
class LoginView(APIView):
    def post(self,request,format=None):
        serilizer = Login(data=request.data)
        if serilizer.is_valid():
            email = serilizer.validated_data.get("email")
            password = serilizer.validated_data.get("password")
            user = authenticate(email=email,password=password)
            if user is not None:
                return Response("sucessfully Login",status=status.HTTP_200_OK)
            else:
                return Response("invalid user",status=status.HTTP_400_BAD_REQUEST)
        return Response(serilizer.errors)
