from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Pet(models.Model):
    PET_TYPES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('BIRD', 'Bird'),
        ('RABBIT', 'Rabbit'),
        ('OTHER', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=10, choices=PET_TYPES)
    age_months = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(240)]  # Max 20 years
    )
    breed = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_adopted = models.BooleanField(default=False)
    adoption_fee = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Validation: fee cannot be negative
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_pet_type_display()})"
    
    class Meta:
        ordering = ['-created_at']