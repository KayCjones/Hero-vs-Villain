from django.db import models
from super_types.models import SuperType

# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)
    super_type = models.ForeignKey(SuperType,on_delete=models.CASCADE)