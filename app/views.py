from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from .models import Venue,User
from .serializers import VenueSerializers

# ✅ Add a Venue
class AddVenueView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            organizer = User.objects.get(user=request.user)
            data = request.data.copy()
            data["organizer"] = organizer.pk  # Set the organizer ID
            serializer = VenueSerializers(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Venue added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "You must be an organizer to add a venue"}, status=status.HTTP_403_FORBIDDEN)


# ✅ Update Venue
class UpdateVenueView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, venue_id):
        try:
            venue = Venue.objects.get(pk=venue_id, organizer__user=request.user)
            serializer = VenueSerializers(venue, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Venue updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Venue.DoesNotExist:
            return Response({"error": "Venue not found or unauthorized"}, status=status.HTTP_404_NOT_FOUND)


# ✅ Delete Venue
class DeleteVenueView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, venue_id):
        try:
            venue = Venue.objects.get(pk=venue_id, organizer__user=request.user)
            venue.delete()
            return Response({"message": "Venue deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Venue.DoesNotExist:
            return Response({"error": "Venue not found or unauthorized"}, status=status.HTTP_404_NOT_FOUND)


# ✅ List All Venues (Anyone can view)
class ListVenuesView(ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializers


# ✅ Get Venue Details
class GetVenueDetailsView(RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializers
    lookup_field = "venue_id"
