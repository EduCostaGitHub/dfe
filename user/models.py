from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    ''' User of the app'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    cc = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    local = models.CharField(max_length=50)
    district = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Profiles'
