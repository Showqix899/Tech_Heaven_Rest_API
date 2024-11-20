#from django 
from django.urls import path,include

#from views
from .views import (
    GetDesktop,GetGamingDesktop,LaptopView,GamingLaptopView,
    DesktopRamView,LaptopRamView,ImacView,MackbookView,CpuCoolerView,Processorview,
    MotherBoardView,HardDriveView,SolidDriveView,GraphicsCardView,PowerSupplyView
)
#from rest_framework
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'laptop',LaptopView,basename="laptop")
router.register(r'gaminglaptop',GamingLaptopView,basename="gaminglaptop")
router.register(r'desktopram',DesktopRamView,basename="desktopram")
router.register(r'laptopram',LaptopRamView,basename="laptopram")
router.register(r'imac',ImacView,basename="imac")
router.register(r'mackbook',MackbookView,basename="mackbook")
router.register(r'cpucooler',CpuCoolerView,basename="cpucooler")
router.register(r'processor',Processorview,basename="processore")
router.register(r'motherboard',MotherBoardView,basename="motherboard")
router.register(r'hdd',HardDriveView,basename="hdd")
router.register(r'ssd',SolidDriveView,basename="ssd")
router.register(r'graphics_card',GraphicsCardView,basename="graphics_card")
router.register(r'power_supply',PowerSupplyView,basename="power_supply")



urlpatterns = [
    path('desktop',GetDesktop.as_view(),name="desktop"),
    #for update and delete
    path('desktop/<str:id>/',GetDesktop.as_view(),name="desktop"),
    path('gamingdesktop',GetGamingDesktop.as_view(),name="gamingdesktop"),
    #to update and delete
    path('gamingdesktop/<str:int>/',GetGamingDesktop.as_view(),name="gamingdesktop"),
    
    path('',include(router.urls)),
]
