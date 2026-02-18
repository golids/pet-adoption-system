from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Pet

class PetAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.pet_data = {
            'name': 'Max',
            'pet_type': 'DOG',
            'age_months': 24,
            'breed': 'Golden Retriever',
            'description': 'Friendly dog',
            'is_adopted': False,
            'adoption_fee': '150.00'
        }
    
    def test_create_pet(self):
        """Test creating a new pet"""
        url = reverse('v1:pet-list', kwargs={'version': 'v1'})
        response = self.client.post(url, self.pet_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pet.objects.count(), 1)
        self.assertEqual(Pet.objects.get().name, 'Max')
    
    def test_invalid_age_negative(self):
        """Test validation - negative age should fail"""
        url = reverse('v1:pet-list', kwargs={'version': 'v1'})
        invalid_data = self.pet_data.copy()
        invalid_data['age_months'] = -5
        
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_invalid_fee_negative(self):
        """Test validation - negative fee should fail"""
        url = reverse('v1:pet-list', kwargs={'version': 'v1'})
        invalid_data = self.pet_data.copy()
        invalid_data['adoption_fee'] = '-50.00'
        
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)