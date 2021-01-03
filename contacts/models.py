from django.db import models

# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
# Create your models here.
class Contact(models. Model):
    name = models.CharField(max_length=255)
    phone_no = PhoneNumberField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.phone_no)

    def get_absolute_url(self):
        return reverse('send-message', kwargs={"pk": self.pk})

