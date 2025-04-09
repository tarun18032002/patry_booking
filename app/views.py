from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from .Custompermissions import IsOrganizer
from rest_framework.response import Response
from rest_framework import status
from .models import Venue
from .serializers import VenueSerializers
from django.shortcuts import get_object_or_404

class VenueCreate(ViewSet):
    permission_classes = [IsAuthenticated,IsOrganizer]
    
    def create(self,request):
        serilaizers = VenueSerializers(data= request.data,context={'request': request})
        if serilaizers.is_valid():
            serilaizers.save(organizer=request.data)
            return Response(serilaizers.data, status=status.HTTP_201_CREATED)
        return Response(serilaizers.errors,status=status.HTTP_400_BAD_REQUEST)

class VenueList(ViewSet):
 
    permission_classes = [IsAuthenticated,AllowAny]
    def list(self,request):
        if request.user.role == 'organizer':
            venue = Venue.objects.filter(organizer = request.user)
        else:
            venue = Venue.objects.all()
        serilizers = VenueSerializers(venue,many=True)
        return Response(serilizers.data,status=status.HTTP_200_OK)
    
class VenueDetail(ViewSet):
    permission_classes = [IsAuthenticated,IsOrganizer]

    def retrieve(self,request,pk=None):
        try:
            venue = Venue.objects.get(pk=pk, organizer=request.user)
            serializer = VenueSerializers(venue)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Venue.DoesNotExist:
            return Response({'message': 'Venue not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self,request,pk=None):
        try:
            venue = Venue.objects.get(pk=pk,organizer=request.user)
            serilizers = VenueSerializers(venue,data=request.data,context={'request': request})
            if serilizers.is_valid():
                serilizers.save()
                return Response(serilizers.data,status=status.HTTP_200_OK)
            return Response(serilizers.errors,status=status.HTTP_400_BAD_REQUEST)
        except Venue.DoesNotExist:
            return Response({'message':'Venue is not updated!'},status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self,request,pk=None):
        try:
            venue = Venue.objects.get(pk=pk,organizer= request.user)
            venue.delete()
            return Response({'message':'Venue is deleted!'},status=status.HTTP_204_NO_CONTENT)
        except Venue.DoesNotExist:
            return Response({'message':'Venue is not deleted!'},status=status.HTTP_404_NOT_FOUND)
        