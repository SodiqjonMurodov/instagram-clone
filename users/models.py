from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import BaseModel

ORDINARY_USER, MANAGER, ADMIN = ('Ordinary User', 'Manager', 'Admin')
VIA_EMAIL, VIA_PHONE_NUMBER = ('Via Email', 'Via Phone Number')
NEW, CODE_VERIFIED, DONE = ('New', 'Code Verified', 'Done')
MALE, FEMALE, OTHER = ('Male', 'Female', 'Other')

class User(AbstractUser, BaseModel):
    USER_ROLE_CHOICES = (
        (ORDINARY_USER, ORDINARY_USER),
        (MANAGER, MANAGER),
        (ADMIN, ADMIN),
    )
    AUTH_TYPE_CHOICES = (
        (VIA_EMAIL, VIA_EMAIL),
        (VIA_PHONE_NUMBER, VIA_PHONE_NUMBER),
    )
    AUTH_STATUS_CHOICES = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
    )
    GENDER_CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER),
    )

    user_role = models.CharField(max_length=31, choices=USER_ROLE_CHOICES, default=ORDINARY_USER)
    AUTH_TYPE = models.CharField(max_length=31, choices=AUTH_TYPE_CHOICES)
    AUTH_STATUS = models.CharField(max_length=31, choices=AUTH_STATUS_CHOICES, default=NEW)
    gender = models.CharField(max_length=31, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    photo = models.ImageField(upload_to='user_photos/%Y/%m/%d/', blank=True, null=True, default='default-avatar.jpg')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'