from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerilizer,UserRegisterSerializer,AdminUserSerializer
from .Custompermissions import IsAdminUser,IsOwnerorAdmin


class UserRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated,IsOwnerorAdmin]

    def list(self,request):
        if request.user.role == 'admin':
            # Admin can see all users
            users = User.objects.all()
            serilaizers = AdminUserSerializer(users,many=True)
            return Response(serilaizers.data)
        else:
            # User and organizers can only see themselves

            serilaizers = UserSerilizer(request.user)
            return Response(serilaizers.data)
        

    def retrieve(self,request,pk=None):
        user = get_object_or_404(User,pk=pk)
        self.check_object_permissions(request, user)
        if request.user.role =='admin':
            serilaizer = AdminUserSerializer(user)
        else :
            serilaizer = UserSerilizer(user)
        return Response(serilaizer.data)
    
    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        
        serializer = UserSerilizer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        if request.user.role != 'admin':
            return Response({"detail": "Only admin can delete accounts"}, 
                            status=status.HTTP_403_FORBIDDEN)
        
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = UserSerilizer(request.user)
        return Response(serializer.data)