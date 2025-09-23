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

    league_details = LeagueSerializer(source='league', read_only=True)
    country_details = CountrysSerializer(source='country', read_only=True)
    #for many to many relation
    characteristics_names = serializers.SerializerMethodField()

    class Meta:
        model = FootballClub
        fields  = '__all__'

    def get_characteristics_names(self,obj):
        return [char.name for char in obj.characteristics.all()]#get only field characteristics  from  'FootballClub'