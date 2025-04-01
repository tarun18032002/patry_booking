from django.db import models
from django.contrib.auth.models import User
import uuid

# Organizer Model
class Organizer(models.Model):
    organizer_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer")
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
# Admin Model (Optional if you need separate roles)
class AdminProfile(models.Model):
    admin_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")
    role = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.user.username

# Venue Model
class Venue(models.Model):
    venue_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name="venues")
    name = models.CharField(max_length=255)
    location = models.TextField()
    capacity = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Party Booking Model
class Party(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    party_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parties")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="bookings")
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Party at {self.venue.name} on {self.event_date}"

# Payment Model
class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    payment_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="payments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username}"

# Review Model
class Review(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating}⭐"


