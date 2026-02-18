from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Pet
from .serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing pets.
    Supports full CRUD operations.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]  # For testing; use proper auth in production
    
    def get_queryset(self):
        """Optional filtering by adoption status"""
        queryset = Pet.objects.all()
        adopted = self.request.query_params.get('adopted', None)
        if adopted is not None:
            queryset = queryset.filter(is_adopted=adopted.lower() == 'true')
        return queryset