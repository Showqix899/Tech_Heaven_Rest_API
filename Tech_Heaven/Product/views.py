from django.shortcuts import render
from django.shortcuts import get_object_or_404

#from model
from .models import (Desktop,GamingDesktop,Laptop,GamingLaptop,Laptop_Ram,
                     DekstopRam,Mackbook,ImacDekstop,CpuCooler,MotherBoard,HardDrive,SolidDrive,
                     Processore,GraphicsCard,PowerSupply)

#from serializers
from .serializers import (
                          DesktopSerializer,GamingDesktopSerializer,GamingLaptopSerializer,LaptopSerializer,
                          ImacDesktopSerializer,MacbookSerializer,PowerSupplySerializer,CpuCoolerSerializer,LaptopRamSerializer,DesktopRamSerializer,
                          SolidDriveSerializer,HardDriveSerializer,MotherBoardSerializer,ProcessorSerializer,GraphicsCardSerializer
                          )
#from rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets



#for get all the dekstip
class GetDesktop(APIView):
    #to get data from Desktop data table
    def get(self,request):

        desktops=Desktop.objects.all()
        if desktops:
            serializer=DesktopSerializer(desktops,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("there is no item")
    
    #to post data in database
    def post(self,request):
        desktop=request.data
        serializer=DesktopSerializer(data=desktop)

        if serializer.is_valid(): #if the serializer is valid
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    #to update
    def put(self,request,id):
        desktop=get_object_or_404(Desktop,id=id)
        serializer=DesktopSerializer(desktop,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(status=status.HTTP_418_IM_A_TEAPOT)
    
    #to delete
    def delete(self,request,id):
        desktop=get_object_or_404(Desktop,id=id)
        desktop.delete()


    

#for get all the dekstip
class GetGamingDesktop(APIView):
    #to get data from Desktop data table
    def get(self,request):

        gaming_desktop=GamingDesktop.objects.all()
        serializer=GamingDesktopSerializer(gaming_desktop,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #to post data in database
    def post(self,request):
        gaming_desktop=request.data
        serializer=GamingDesktopSerializer(data=gaming_desktop)

        if serializer.is_valid(): #if the serializer is valid
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #to update
    def put(self,request,id):
        gaming_desktop=get_object_or_404(GamingDesktop,id=id)
        serializer=GamingDesktopSerializer(GamingDesktop,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(status=status.HTTP_418_IM_A_TEAPOT)
    
    #to delete
    def delete(self,request,id):
        desktop=get_object_or_404(GamingDesktop,id=id)
        desktop.delete()
    

#for laptop

class LaptopView(viewsets.ModelViewSet):

    serializer_class=LaptopSerializer
    queryset=Laptop.objects.all()

#for gaming laptop

class GamingLaptopView(viewsets.ModelViewSet):

    serializer_class=GamingLaptopSerializer
    queryset=GamingLaptop.objects.all()



#for Imac pc
class ImacView(viewsets.ModelViewSet):

    serializer_class=ImacDesktopSerializer
    queryset=ImacDekstop.objects.all()


#for mackbook
class MackbookView(viewsets.ModelViewSet):

    serializer_class=MacbookSerializer
    queryset=Mackbook.objects.all()

#for Desktop ram
class DesktopRamView(viewsets.ModelViewSet):

    serializer_class=DesktopRamSerializer
    queryset=DekstopRam.objects.all()

#for Laptop ram
class LaptopRamView(viewsets.ModelViewSet):

    serializer_class=LaptopRamSerializer
    queryset=Laptop_Ram.objects.all()

#for Cpu cooler
class CpuCoolerView(viewsets.ModelViewSet):

    serializer_class=CpuCoolerSerializer
    queryset=CpuCooler.objects.all()


#for Processore
class Processorview(viewsets.ModelViewSet):

    serializer_class=ProcessorSerializer
    queryset=Processore.objects.all()

#for motherboard
class MotherBoardView(viewsets.ModelViewSet):

    serializer_class=MotherBoardSerializer
    queryset=MotherBoard.objects.all()

#for hard drive
class HardDriveView(viewsets.ModelViewSet):
    
    serializer_class=HardDriveSerializer
    queryset=HardDrive.objects.all()

#for SDD
class SolidDriveView(viewsets.ModelViewSet):

    serializer_class=SolidDriveSerializer
    queryset=SolidDrive.objects.all()

#for graphics card
class GraphicsCardView(viewsets.ModelViewSet):

    serializer_class=GraphicsCardSerializer
    queryset=GraphicsCard.objects.all()

#for Power supply
class PowerSupplyView(viewsets.ModelViewSet):

    serializer_class=PowerSupplySerializer
    queryset=PowerSupply.objects.all()