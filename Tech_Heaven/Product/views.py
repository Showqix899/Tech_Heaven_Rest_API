from django.shortcuts import render

#from model
from .models import Desktop

#from serializers
from .serializers import DesktopSerializer

#from rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#for get all the dekstip
class GetDesktop(APIView):

    def get(self,request):

        desktops=Desktop.objects.all()
        serializer=DesktopSerializer(desktops,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)