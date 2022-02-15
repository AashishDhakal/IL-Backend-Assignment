from django.db import models

# Create your models here.


class MyModel(models.Model):
    # sample model to implement filter
    date = models.DateField(help_text='date created')
    distance = models.IntegerField(help_text='distance')
