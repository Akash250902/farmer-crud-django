from django.db import models

# Create your models here.
class Farmer_Form(models.Model):
    farmer_id=models.IntegerField()
    farmer_name=models.CharField(max_length=20)
    f_state=models.CharField(max_length=20)
    f_district=models.CharField(max_length=20)
    f_age=models.CharField(max_length=20)
    f_contact=models.CharField(max_length=10)
    f_email=models.EmailField()
    f_crop=models.CharField(max_length=20)
    f_quantity=models.IntegerField()
    
    def __str__ (self):
        return str(self.farmer_name)