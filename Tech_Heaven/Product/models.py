
#form django
from django.db import models
from django.utils.timezone import now

#python
import uuid

# Create your models here.

product_catagories=[('DEKSTOP',"DEKSTOP"),('GAMINGDEKSTOP',"GAMINGDEKSTOP"),("IMAC","IMAC")]


#desktop
class Desktop(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    processore=models.CharField(max_length=400,default="blank")
    monitor=models.CharField(max_length=200,default="N/A")
    motherboard=models.CharField(max_length=400,default="blank")
    keyboard=models.CharField(max_length=200,default="N/A")
    mouse=models.CharField(max_length=200,default="N/A")
    ram=models.CharField(max_length=400,default="blank")
    storage=models.CharField(max_length=400,default="blank")
    networks_wireless_conections=models.CharField(max_length=400,null=True,blank=True)
    operating_system=models.CharField(max_length=100,default="N/A")
    power_supply=models.CharField(max_length=400,null=True,blank=True)
    cpu_cooler=models.CharField(max_length=400,null=True,blank=True)
    casing=models.CharField(max_length=400,default="blank")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=2)
    discount_price=models.DecimalField(max_digits=10,decimal_places=2)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_code=models.CharField(max_length=200,null=True,blank=True)
    product_release=models.DateTimeField(auto_now_add=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")
    
    #overiding the save method for generating product code
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
    monitor=models.CharField(max_length=200,default="N/A")
    motherboard=models.CharField(max_length=400,default="blank")
    keyboard=models.CharField(max_length=200,default="N/A")
    mouse=models.CharField(max_length=200,default="N/A")
    ram=models.CharField(max_length=400,default="blank")
    graphics_card=models.CharField(max_length=400,null=True,blank=True)
    storage=models.CharField(max_length=400,default="blank")
    networks_wireless_conections=models.CharField(max_length=400,null=True,blank=True)
    operating_system=models.CharField(max_length=100,default="N/A")
    power_supply=models.CharField(max_length=400,null=True,blank=True)
    cpu_cooler=models.CharField(max_length=400,null=True,blank=True)
    casing=models.CharField(max_length=400,default="blank")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_code=models.CharField(max_length=200,null=True,blank=True)
    product_release=models.DateTimeField(auto_now_add=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")


    #overiding the save method for generating product code
    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"D{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    



#apple Imac Dekstop

class ImacDekstop(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    processore=models.CharField(max_length=400,default="blank")
    monitor=models.CharField(max_length=200,default="N/A")
    motherboard=models.CharField(max_length=400,default="blank")
    keyboard=models.CharField(max_length=200,default="N/A")
    ram=models.CharField(max_length=400,default="blank")
    graphics_card=models.CharField(max_length=400,null=True,blank=True)
    storage=models.CharField(max_length=400,default="blank")
    networks_wireless_conections=models.CharField(max_length=400,null=True,blank=True)
    operating_system=models.CharField(max_length=100,default="N/A")
    power_supply=models.CharField(max_length=400,null=True,blank=True)
    cpu_cooler=models.CharField(max_length=400,null=True,blank=True)
    casing=models.CharField(max_length=400,default="blank")
    color=models.CharField(max_length=100,default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_code=models.CharField(max_length=200,null=True,blank=True)
    product_release=models.DateTimeField(auto_now_add=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    #overiding the save method for generating product code
    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"IM{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    



# Laptop

class Laptop(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    processore=models.CharField(max_length=400,default="blank")
    processore_frequency=models.CharField(max_length=50,default="N/A")
    processore_core=models.CharField(max_length=30,default="N/A")
    processore_thread=models.CharField(max_length=30,default="N/A")
    cpu_cache=models.CharField(max_length=30,default="N/A")
    display=models.CharField(max_length=100,default="N/A")
    refresh_rate=models.CharField(max_length=10,default="N/A")
    ram=models.CharField(max_length=20)
    ram_type=models.CharField(max_length=30)
    ram_slot=models.IntegerField(default=1)
    ram_capacity=models.IntegerField(default=8)
    operating_system=models.CharField(max_length=100,default="N/A")
    storege=models.IntegerField(default=128)
    storege_type=models.CharField(max_length=30,default="M.2")
    storege_slot=models.IntegerField(default=1)
    graphix_model=models.CharField(max_length=30,default="N/A")
    graphics_memory=models.CharField(max_length=30,default="shared")
    keyboard_type=models.CharField(max_length=30,default="N/A")
    touchpad=models.BooleanField(default=False)
    camera=models.CharField(max_length=30,default="N/A")
    microphone=models.BooleanField(default=False)
    speaker=models.BooleanField(default=False)
    optical_drive=models.CharField(max_length=30,default="N/A")
    card_reader=models.CharField(max_length=30,default="N/A")
    usb_ports=models.CharField(max_length=100,default="N/A")
    headphone_jack=models.BooleanField(default=False)
    network_wifi=models.CharField(max_length=100,default="N/A")
    fringerprint_sensore=models.BooleanField(default=False)
    battery=models.CharField(max_length=100,default="N/A")
    battery_capacity=models.CharField(max_length=100,default="N/A")
    dimension=models.CharField(max_length=100,default="N/A")
    weight=models.CharField(max_length=100,default="N/A")
    body_metarial=models.CharField(max_length=100,default="N/A")
    color=models.CharField(max_length=100,default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"IM{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title

#gaming laptop

class GamingLaptop(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    processore=models.CharField(max_length=400,default="blank")
    processore_frequency=models.CharField(max_length=50,default="N/A")
    processore_core=models.CharField(max_length=30,default="N/A")
    processore_thread=models.CharField(max_length=30,default="N/A")
    cpu_cache=models.CharField(max_length=30,default="N/A")
    display=models.CharField(max_length=100,default="N/A")
    refresh_rate=models.CharField(max_length=10,default="N/A")
    ram=models.CharField(max_length=20)
    ram_type=models.CharField(max_length=30)
    ram_slot=models.IntegerField(default=1)
    ram_capacity=models.IntegerField(default=8)
    operating_system=models.CharField(max_length=100,default="N/A")
    storege=models.IntegerField(default=128)
    storege_type=models.CharField(max_length=30,default="M.2")
    storege_slot=models.IntegerField(default=1)
    graphics_card=models.CharField(max_length=400,null=True,blank=True)
    keyboard_type=models.CharField(max_length=30,default="N/A")
    touchpad=models.BooleanField(default=False)
    camera=models.CharField(max_length=30,default="N/A")
    microphone=models.BooleanField(default=False)
    speaker=models.BooleanField(default=False)
    optical_drive=models.CharField(max_length=30,default="N/A")
    card_reader=models.CharField(max_length=30,default="N/A")
    usb_ports=models.CharField(max_length=100,default="N/A")
    headphone_jack=models.BooleanField(default=False)
    network_wifi=models.CharField(max_length=100,default="N/A")
    fringerprint_sensore=models.BooleanField(default=False)
    battery=models.CharField(max_length=100,default="N/A")
    battery_capacity=models.CharField(max_length=100,default="N/A")
    dimension=models.CharField(max_length=100,default="N/A")
    weight=models.CharField(max_length=100,default="N/A")
    body_metarial=models.CharField(max_length=100,default="N/A")
    color=models.CharField(max_length=100,default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"IM{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title