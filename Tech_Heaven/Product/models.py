
#form django
from django.db import models
from django.utils.timezone import now

#python
import uuid

# Create your models here.


#desktop
class Desktop(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    processore=models.CharField(max_length=400,default="blank")
    motherboard=models.CharField(max_length=400,default="blank")
    ram=models.CharField(max_length=400,default="blank")
    storage=models.CharField(max_length=400,default="blank")
    power_supply=models.CharField(max_length=400,null=True,blank=True)
    cpu_cooler=models.CharField(max_length=400,null=True,blank=True)
    casing=models.CharField(max_length=400,default="blank")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=7,decimal_places=3)
    discount_price=models.DecimalField(max_digits=7,decimal_places=3)
    product_code=models.CharField(max_length=200,null=True,blank=True)
    product_release=models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"D{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title





#gaming desktop
class GamingDesktop(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    processore=models.CharField(max_length=400,default="blank")
    motherboard=models.CharField(max_length=400,default="blank")
    ram=models.CharField(max_length=400,default="blank")
    graphics_card=models.CharField(max_length=400,null=True,blank=True)
    storage=models.CharField(max_length=400,default="blank")
    power_supply=models.CharField(max_length=400,null=True,blank=True)
    cpu_cooler=models.CharField(max_length=400,null=True,blank=True)
    casing=models.CharField(max_length=400,default="blank")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=7,decimal_places=3)
    discount_price=models.DecimalField(max_digits=7,decimal_places=3)
    product_code=models.CharField(max_length=200,null=True,blank=True)
    product_release=models.DateTimeField(auto_now_add=True)

    #overiding the save method for generating 
    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"D{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    



