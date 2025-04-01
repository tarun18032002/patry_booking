from django.contrib import admin
from .models import AdminProfile,Organizer,Party,Payment,Review,User,Venue

# Register your models here.
admin.site.register(AdminProfile)
admin.site.register(Organizer)
admin.site.register(Party)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Venue)