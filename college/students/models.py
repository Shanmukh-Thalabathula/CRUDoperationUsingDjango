from django.db import models

# Create your models here.
class Students(models.Model):
    profile = models.ImageField(null=True,blank=True,upload_to='profiles/')
    full_name = models.CharField(max_length=100)
    pin_no = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    gmail = models.EmailField()
    branch = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.full_name