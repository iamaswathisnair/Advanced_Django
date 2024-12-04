from django.db import models
  # Gender field (choice-based)
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
   

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
# Radio buttons: This is the default behavior when using choices with a CharField in Django forms.
    )
    class Meta:
        db_table = 'custom_user_table'  # SQL table name
        verbose_name = "user reg"       # Admin-friendly name