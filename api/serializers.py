from rest_framework import serializers
from .models import Pet
from datetime import date

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def validate_age_months(self, value):
        """Custom validation: age cannot be negative and reasonable max"""
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative!")
        if value > 240:  # 20 years in months
            raise serializers.ValidationError("Age seems too high for a pet!")
        return value
    
    def validate_adoption_fee(self, value):
        """Validation: adoption fee cannot be negative"""
        if value < 0:
            raise serializers.ValidationError("Adoption fee cannot be negative!")
        if value > 10000:
            raise serializers.ValidationError("Adoption fee seems too high!")
        return value
    
    def validate_name(self, value):
        """Validation: name should be at least 2 characters"""
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long!")
        return value