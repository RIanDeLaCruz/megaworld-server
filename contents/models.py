from django.db import models

from tinymce import models as tinymce_models
from location_field.models.plain import PlainLocationField


class Content(models.Model):
    HOME = 'HO'
    ABOUT = 'AB'
    TOWN = 'TO'
    PRESELL = 'PR'
    READY = 'RE'
    UPDATE = 'UP'
    CONTACT = 'CO'

    PAGE_CHOICES = (
        (HOME, 'Home'),
        (ABOUT, 'About'),
        (TOWN, 'Town'),
        (PRESELL, 'Presell'),
        (READY, 'Ready'),
        (UPDATE, 'Update'),
        (CONTACT, 'Contact')
    )

    name = models.TextField()
    page = models.CharField(
        max_length=2,
        choices=PAGE_CHOICES,
        default=HOME
    )
    content = tinymce_models.HTMLField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class UnitType(models.Model):
    name = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Location(models.Model):
    name = models.TextField()
    geocode = PlainLocationField(based_fields=['city'], zoom=7)

class Property(models.Model):
    READY = 'RE'
    PRESELLING = 'PRE'

    COMPLETION_CHOICES = (
        (READY, 'Ready'),
        (PRESELLING, 'Pre-Selling')
    )

    name = models.TextField()
    completion_statis = models.CharField(
        max_length=3,
        choices=COMPLETION_CHOICES,
        default=READY
    )
    completion_date = models.TextField()
    unit_type = models.ForeignKey(
        'UnitType',
        on_delete=models.CASCADE,
        related_name='properties'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        related_name='properties'
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class PropertyImage(models.Model):
    mw_property = models.ForeignKey(
        'Property',
        on_delete=models.SET_NULL,
        null=True,
        related_name='images'
    )
    image = models.FileField()
    is_primary = models.BooleanField(
        default=False
    )
