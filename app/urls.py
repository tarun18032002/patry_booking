from django.urls import path
from .views import AddVenueView, UpdateVenueView, DeleteVenueView, ListVenuesView, GetVenueDetailsView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .UserViews import UserRegistrationViewSet, UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('venues/add', AddVenueView.as_view(), name='add_venue'),
    path('venues/update/<uuid:venue_id>', UpdateVenueView.as_view(), name='update_venue'),
    path('venues/delete/<uuid:venue_id>', DeleteVenueView.as_view(), name='delete_venue'),
    path('venues/', ListVenuesView.as_view(), name='list_venues'),
    path('venues/<uuid:venue_id>', GetVenueDetailsView.as_view(), name='get_venue_details'),
    path('', include(router.urls)),
    path('register/', UserRegistrationViewSet.as_view({'post': 'create'}), name='register'),
    path('me/', UserViewSet.as_view({'get': 'me'}), name='me'),
]




