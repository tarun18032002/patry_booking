from rest_framework import serializers
from .models import User,Party,Payment,Review,Venue
from rest_framework.authtoken.models import Token

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','role']
        read_only_fields = ['role']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
    password_confirm = serializers.CharField(write_only=True,required = True,style={'input_type':'password'})

    class Meta:
        model = User
        fields = ['username','email','password','password_confirm','first_name','last_name','role']

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('password_confirm'):
            raise serializers.ValidationError({'password':"Password fields didn't match."})
    
        return attrs

    def create(self,validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'user')
        )
        return user
    

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role',  'is_active']
        
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

class VenueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
        read_only_fields = ['organizer', 'venue_id', 'created_at'] 

    def create(self,validated_data):
        request = self.context.get('request')
        print(request.user)
        validated_data['organizer']= request.user
        return super().create(validated_data)
    
    def update(self,instance,validated_data):
        request = self.context.get('request')
        validated_data['oragnizer']=request.user
        return super().update(instance,validated_data)