from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.core.validators import RegexValidator



# Create your models here.

class Contacts(models.Model):
    company_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email= models.EmailField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdcontacts')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''.join([self.company_name,' ', self.first_name, self.last_name])