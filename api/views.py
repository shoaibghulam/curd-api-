# views.py
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserRegistrationSerializer ,AboutSerializer
from .models import About

# views.py

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED, headers=headers)
    

@permission_classes([IsAuthenticated])
class Curd(APIView):
    def get(self,request):
        print("the user is",request.user.id)
        data= About.objects.filter(user_id=request.user)
        ser_data= AboutSerializer(data,many=True)
        return Response(ser_data.data)
    
  
    
    def post(self, request):
        serializer = AboutSerializer(data=request.data)
        
        if serializer.is_valid():
            # Set the user_id based on the currently logged-in user
            serializer.validated_data['user_id'] = request.user

            # Save the instance
            serializer.save()

            return Response({'message': 'About instance created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request,id):
        try:
            # Get the existing About instance based on user_id
            about_instance = About.objects.get(pk=id,user_id=request.user)
        except About.DoesNotExist:
            return Response({'error': 'About instance not found for the current user'}, status=status.HTTP_404_NOT_FOUND)

        # Update the instance with the incoming data
        serializer = AboutSerializer(about_instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            # Save the updated instance
            serializer.save()

            return Response({'message': 'About instance updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request,id):
        try:
            # Get the existing About instance based on user_id
            about_instance = About.objects.get(user_id=request.user)
        except About.DoesNotExist:
            return Response({'error': 'About instance not found for the current user'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user making the request is the owner of the About instance
        if request.user != about_instance.user_id:
            return Response({'error': 'You do not have permission to delete this instance.'}, status=status.HTTP_403_FORBIDDEN)

        about_instance.delete()
        return Response({'message': 'About instance deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
@permission_classes([IsAuthenticated])
class CurdSingle(APIView):
      def get(self,request,id):
        print("the user is",request.user.id)
        data= About.objects.filter(pk=id,user_id=request.user)
        ser_data= AboutSerializer(data,many=True)
        return Response(ser_data.data)
    
  
