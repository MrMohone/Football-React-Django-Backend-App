from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response

class CountryViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Country.objects.all()
    serializer_class = CountrysSerializer

    def list(self,request):
        queryset = Country.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class LeagueViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

    def list(self,request):
        queryset = League.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class CharactersticViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Characterstics.objects.all()
    serializer_class = CharactersticsSerializer

    def list(self,request):
        queryset = Characterstics.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class FootballClubViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = FootballClub.objects.all()
    serializer_class = FootballClubSerializer

    def list(self,request):
        queryset = FootballClub.objects.all()
        serializer = FootballClubSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        queryset = self.queryset.get(pk=pk) #accecssing the primary key
        serializer = FootballClubSerializer(queryset)#many is not required
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        queryset = self.queryset.get(pk=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    