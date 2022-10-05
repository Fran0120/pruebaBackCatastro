from rest_framework import serializers
from movies_information.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('Titulo', 'Calificacion', 'Pais')
        read_only_fields = ("MovieId", )
