from django.db import models
from super_types.models import SuperType


# Create your models here.
class Super(models.Model):
    name= models.CharField(max_length=250)
    alter_ego= models.CharField(max_length=250)
    primary_ability=models.CharField(max_length=250)
    secondary_ability = models.CharField(max_length=250)
    catchphrase=models.CharField(max_length=500)
    super_type=models.ForeignKey(SuperType, on_delete= models.CASCADE)

    
