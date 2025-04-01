from rest_framework import serializers
from .models import AdminProfile,Organizer,Party,Payment,Review,Venue

class adminSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = '__all__'


class OrganizerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'

class PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class VenuewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'