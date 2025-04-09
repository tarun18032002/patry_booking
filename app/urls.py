from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueCreate, VenueDetail,VenueList
from .UserViews import UserRegistrationViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),

    # Venue routes
    path('venues/list/', VenueList.as_view({'get': 'list'}), name='listvenues'),
    path('venues/create/',VenueCreate.as_view({'post': 'create'}), name='createvenues'),
    path('venues/update/<uuid:pk>/', VenueDetail.as_view({'put': 'update'}), name='updatevenues'),
    path('venues/retrieve/<uuid:pk>/', VenueDetail.as_view({'get': 'retrieve'}), name='retrievevenues'),
    path('venues/delete/<uuid:pk>/', VenueDetail.as_view({'delete': 'destroy'}), name='deletevenues'),

    # Auth routes
    path('register/', UserRegistrationViewSet.as_view({'post': 'create'}), name='register'),
    path('me/', UserViewSet.as_view({'get': 'me'}), name='me'),
]



