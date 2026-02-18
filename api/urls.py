from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet

# Create router
router = DefaultRouter()
router.register(r'pets', PetViewSet, basename='pet')

# Versioned URLs
urlpatterns = [
    # API version 1
    path('v1/', include((router.urls, 'api'), namespace='v1')),
]