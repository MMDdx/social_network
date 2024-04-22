from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterationSerializer


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterationSerializer




