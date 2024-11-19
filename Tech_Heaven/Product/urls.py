#from django 
from django.urls import path

#from views
from .views import GetDesktop

urlpatterns = [
    path('desktop',GetDesktop.as_view(),name="desktop"),
]
