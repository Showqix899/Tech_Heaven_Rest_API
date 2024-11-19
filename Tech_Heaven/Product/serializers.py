from rest_framework import serializers

# from models
from .models import (
    Desktop, DesktopRam, GamingDesktop, Laptop, Laptop_Ram, GamingLaptop, PowerSupply,
    Processor, SolidDrive, HardDrive, CpuCooler, Macbook, ImacDesktop, MotherBoard
)

# Desktop data being serialized and deserialized
class DesktopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desktop
        fields = '__all__'

# Desktop RAM data being serialized and deserialized
class DesktopRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesktopRam
        fields = '__all__'

# Gaming Desktop data being serialized and deserialized
class GamingDesktopSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamingDesktop
        fields = '__all__'

# Laptop data being serialized and deserialized
class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

# Laptop RAM data being serialized and deserialized
class LaptopRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop_Ram
        fields = '__all__'

# Gaming Laptop data being serialized and deserialized
class GamingLaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamingLaptop
        fields = '__all__'

# Power Supply data being serialized and deserialized
class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupply
        fields = '__all__'

# Processor data being serialized and deserialized
class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'

# Solid Drive data being serialized and deserialized
class SolidDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolidDrive
        fields = '__all__'

# Hard Drive data being serialized and deserialized
class HardDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardDrive
        fields = '__all__'

# CPU Cooler data being serialized and deserialized
class CpuCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuCooler
        fields = '__all__'

# MacBook data being serialized and deserialized
class MacbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macbook
        fields = '__all__'

# iMac Desktop data being serialized and deserialized
class ImacDesktopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImacDesktop
        fields = '__all__'

# MotherBoard data being serialized and deserialized
class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = '__all__'
