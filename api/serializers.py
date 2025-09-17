from rest_framework import serializers
from .models import *

class CountrysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields  = ('id', 'name')

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields  = ('id', 'name')

class CharactersticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characterstics
        fields  = ('id', 'name')

class FootballClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballClub
        fields  = '__all__'