from rest_framework import viewsets, permissions, filters, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from collections import Counter

from .models import Movie
from .serializers import MovieSerializer
from .paginations import CustomPagination

class moviesInformationViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('Titulo', 'Calificacion', 'Pais')
    filter_fields = ('Titulo', 'Calificacion', 'Pais')
    ordering_fields = ('MovieId', 'Titulo', 'Calificacion', 'Pais')
    pagination_class = CustomPagination

    def list(self, request):
        if(Response.status_code == 200):
            datos = self.queryset.values('MovieId', "Titulo", "Calificacion", "Pais")
            d = []
            for dato in datos:
                d.append(dato)
            
            output = {
                "success": True,
                "data": d
            }
            return Response(output)
        else:
            output = {
                "success": False,
                "data": []
            }
            return Response(output)

    @action(detail=False, methods=['get'], url_path='summary')
    def summary(self, request):
        if(Response.status_code == 200):
            datos = self.queryset.values('MovieId', "Titulo", "Calificacion", "Pais")
            dataset = []
            paises = []
            resultado = []
            for dato in datos:
                dataset.append(dato)
            for p in range(len(dataset)):
                paises.append(dataset[p]['Pais'])
            paises = list(set(paises))

            for i in range(len(paises)):
                x = dataset.count(dataset[i]['Pais'])
                print(x)

            output = {
                "success": True,
                "data": resultado
            }
            return Response(output)
        else:
            output = {
                "success": False,
                "data": []
            }
            return Response(output)

    @action(detail=False, methods=['get'], url_path='top')
    def top(self, request):
        if(Response.status_code == 200):
            datos = self.queryset.values('MovieId', "Titulo", "Calificacion", "Pais")
            d = []
            resultado = []
            for dato in datos:
                d.append(dato)
            for dato in range(len(d)):
                if(d[dato]['Calificacion'] > 6):
                    resultado.append(d[dato])
            print(resultado)
            output = {
                "success": True,
                "data": resultado
            }
            return Response(output)
        else:
            output = {
                "success": False,
                "data": []
            }
            return Response(output)