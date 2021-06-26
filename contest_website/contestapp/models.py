from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
# Create your models here.


class user_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_No = models.CharField(max_length=200)


class EmailConfirmed(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key=models.CharField(max_length=500)
    email_confirmed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural='User Email-Confirmed'

@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance=EmailConfirmed(user=instance)
        user_encoded=f'{instance.email}-{dt}'.encode()
        activation_key=hashlib.sha224(user_encoded).hexdigest()
        email_confirmed_instance.activation_key=activation_key
        email_confirmed_instance.save()


class add_contest(models.Model):
    # contest_date = models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    # contest_time = models.TimeField(auto_now_add=False, blank=True)
    contest_date = models.CharField(max_length=200, default='YYYY-MM-DD', help_text = "Date Format: <b><em>YYYY-MM-DD</em></b>.")
    contest_time = models.CharField(max_length=200, default='18:00:00', help_text = "Time Format: <b><em>24:00:00</em></b>.")
    price_money = models.CharField(max_length=200)
    entry_money = models.CharField(max_length=200)
