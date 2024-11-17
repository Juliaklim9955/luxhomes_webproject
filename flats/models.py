from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
#import multi selection option:
# from multiselectfield import MultiSelectField


# Create your models here.
class Flat(models.Model):
    
    state_choice = (
            ('AL', 'Alabama'),
            ('AK', 'Alaska'),
            ('AZ', 'Arizona'),
            ('AR', 'Arkansas'),
            ('CA', 'California'),
            ('CO', 'Colorado'),
            ('CT', 'Connecticut'),
            ('DE', 'Delaware'),
            ('DC', 'District Of Columbia'),
            ('FL', 'Florida'),
            ('GA', 'Georgia'),
            ('HI', 'Hawaii'),
            ('ID', 'Idaho'),
            ('IL', 'Illinois'),
            ('IN', 'Indiana'),
            ('IA', 'Iowa'),
            ('KS', 'Kansas'),
            ('KY', 'Kentucky'),
            ('LA', 'Louisiana'),
            ('ME', 'Maine'),
            ('MD', 'Maryland'),
            ('MA', 'Massachusetts'),
            ('MI', 'Michigan'),
            ('MN', 'Minnesota'),
            ('MS', 'Mississippi'),
            ('MO', 'Missouri'),
            ('MT', 'Montana'),
            ('NE', 'Nebraska'),
            ('NV', 'Nevada'),
            ('NH', 'New Hampshire'),
            ('NJ', 'New Jersey'),
            ('NM', 'New Mexico'),
            ('NY', 'New York'),
            ('NC', 'North Carolina'),
            ('ND', 'North Dakota'),
            ('OH', 'Ohio'),
            ('OK', 'Oklahoma'),
            ('OR', 'Oregon'),
            ('PA', 'Pennsylvania'),
            ('RI', 'Rhode Island'),
            ('SC', 'South Carolina'),
            ('SD', 'South Dakota'),
            ('TN', 'Tennessee'),
            ('TX', 'Texas'),
            ('UT', 'Utah'),
            ('VT', 'Vermont'),
            ('VA', 'Virginia'),
            ('WA', 'Washington'),
            ('WV', 'West Virginia'),
            ('WI', 'Wisconsin'),
            ('WY', 'Wyoming'),
        )
    rent_sale_choice = (
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
    )
    
    bedroom_choice = []
    for r in range(1, 10):
        bedroom_choice.append((r,r))
        
    type_choice = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Penthouse', 'Penthouse'),
        ('Entire Building', 'Entrie Building'),
    )
    
    condition_choice = (
        ('Fully Renovated', 'Fully Renovated'),
        ('Basic Renovation', 'Basic Renovation'),
        ('Not Renovated', 'Not Renovated'),
    )

    flat_title = models.CharField(max_length=270)
    state = models.CharField(choices=state_choice, max_length=99)
    city = models.CharField(max_length=99)
    type = models.CharField(choices=type_choice, max_length=99)
    rent_sale = models.CharField(choices=rent_sale_choice, max_length=99)
    bedrooms = models.IntegerField(('bedrooms'), choices=bedroom_choice)
    condition = models.CharField(choices=condition_choice, max_length=99)
    price = models.IntegerField()
    size = models.IntegerField(default=0)
    description = RichTextField()
    flat_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    flat_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    flat_photo2 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    flat_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    flat_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.flat_title










