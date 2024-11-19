
#form django
from django.db import models
from django.utils.timezone import now

#python
import uuid

# Create your models here.




#add all the catagories here
product_catagories=[
                    ('DEKSTOP',"DEKSTOP"),
                    ('GAMINGDEKSTOP',"GAMINGDEKSTOP"),
                    ("IMAC","IMAC"),("LAPTOP","LAPTOP"),
                    ("GAMINGLAPTOP","GAMINGLAPTOP"),
                    ("PROCESSOR","PROCESSOR"),
                    ("CPU COOLER","CPU COOLER"),
                    ("POWER SUPPLY","POWER SUPPLY"),
                    ("HDD","HDD"),
                    ("SDD","SDD"),
                    ("GRAPHICS CARD","GRAPHICA CARD"),
                    ("DEKSTOP RAM","DEKSTOP RAM"),
                    ("LAPTOP RAM","LAPTOP RAM"),
                    ]


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
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"LP{code_initial}00{serial_number}"

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
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"GLP{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title


#apple mackbook

class Mackbook(models.Model):
    
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
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"MB{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title


###########components

class Processore(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    base_frequency=models.CharField(max_length=200,default="blank")
    maximum_frequency=models.CharField(max_length=200,default="blank")
    cache=models.TextField()
    cores=models.CharField(max_length=200,default="blank")
    threads=models.CharField(max_length=20,default="blank")
    maximum_speed=models.CharField(max_length=20,default="blank")
    type=models.CharField(max_length=20,default="blank")
    max_number_channel=models.CharField(max_length=20,default="blank")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"MB{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title


#cpu cooler

class CpuCooler(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    fan_speed=models.CharField(max_length=20,default="blank")
    noise=models.CharField(max_length=20,default="blank")
    connector=models.CharField(max_length=80,default="blank")
    material=models.CharField(max_length=80,default="blank")
    dimension=models.CharField(max_length=80,default="blank")
    weight=models.CharField(max_length=20,default="blank")
    supported_sockets=models.CharField(max_length=80,default="blank")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")


    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"CC{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title



#Motherboard

class MotherBoard(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    supported_gpu=models.TextField()
    chipset=models.CharField(max_length=100,default="N/A")
    audio=models.TextField()
    Expention_Ports=models.TextField()
    memory_type=models.CharField(max_length=100,default="N/A")
    graphics=models.TextField()
    connectors_port=models.TextField()
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"M{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    


#Graphics Card

class GraphicsCard(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    type=models.CharField(max_length=30,default="N/A")
    size=models.CharField(max_length=30,default="N/A")
    core_clock=models.CharField(max_length=100,default="N/A")
    others=models.TextField()
    connectors=models.TextField()
    display_options=models.CharField(max_length=100,default="N/A")
    physical_specification=models.TextField()
    hdmi=models.TextField()
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"GC{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    


#Dekstop_Ram

class DekstopRam(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    type=models.CharField(max_length=30,default="N/A")
    size=models.CharField(max_length=30,default="N/A")
    frequency=models.CharField(max_length=100,default="N/A")
    operating_voltage=models.TextField()
    latency=models.TextField()
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"DRM{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    


#Laptop_Ram

class Laptop_Ram(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    type=models.CharField(max_length=30,default="N/A")
    size=models.CharField(max_length=30,default="N/A")
    frequency=models.CharField(max_length=100,default="N/A")
    operating_voltage=models.TextField(default="N/A")
    latency=models.TextField(default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"LRM{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title
    

#PowerSupply

class PowerSupply(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    power=models.CharField(max_length=30,default="N/A")
    fan_size=models.CharField(max_length=30,default="N/A")
    Lighting_effect=models.CharField(max_length=100,default="N/A")
    input=models.CharField(max_length=30,default="N/A")
    output=models.CharField(max_length=30,default="N/A")
    connectors_port=models.CharField(max_length=30,default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"PS{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title

#HDD

class HardDrive(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    type=models.CharField(max_length=30,default="N/A")
    size=models.CharField(max_length=30,default="N/A")
    interface=models.CharField(max_length=100,default="N/A")
    buffer_size=models.CharField(max_length=30,default="N/A")
    rpm_class=models.CharField(max_length=30,default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"H{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title




#SSD

class SolidDrive(models.Model):

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=True)
    model_title=models.CharField(max_length=200,default="blank")
    brand_name=models.CharField(max_length=200,default="blank")
    type=models.CharField(max_length=30,default="N/A")
    size=models.CharField(max_length=30,default="N/A")
    interface=models.CharField(max_length=100,default="N/A")
    buffer_size=models.CharField(max_length=30,default="N/A")
    rpm_class=models.CharField(max_length=30,default="N/A")
    description=models.TextField(max_length=400)
    status=models.BooleanField(default=False)
    regular_price=models.DecimalField(max_digits=10,decimal_places=3)
    discount_price=models.DecimalField(max_digits=10,decimal_places=3)
    warranty=models.CharField(max_length=1,null=True,blank=True)
    product_catagory=models.CharField(max_length=200,choices=product_catagories,default="N/A")

    def save(self, *args, **kwargs):
        if not self.product_code:  # Ensure product_code is only generated once
            code_initial = self.brand_name[0].upper()
 
            serial_number = Desktop.objects.count() + 1
            self.product_code = f"S{code_initial}00{serial_number}"

        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.model_title