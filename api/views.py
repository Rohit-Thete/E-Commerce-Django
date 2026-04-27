from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer

# Create your views here.
@api_view(["POST"])
def register(request):
    data = request.data
    serializer = RegisterSerializer(data = data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"msg":"User Created","user":{"username":user.username,"email":user.email}},status=201)
    
    return Response(serializer.errors,status=400)



# class UserView(APIView):
#     def get()       


