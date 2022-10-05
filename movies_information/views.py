# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from movies_information.models import Movie
# from movies_information.serializers import MovieSerializer
# # Create your views here.

# @csrf_exempt
# @api_view(["GET", "PUT", "POST", "DELETE"])
# def infoMovieApi(request, id=0):
#     if request.method=='GET':
#         movies = Movie.objects.all()
#         movies_serializer = MovieSerializer.objects.all()
#         movies_serializer = MovieSerializer(movies, many = True)
#         seralized = {'success': True, 'data': ["movies_serializer.data"]}
#         seralizedError = {'success': False, 'data': movies_serializer.data}
#         return Response({'seralized':'MI PERRO'})
#     elif request.method=='POST':
#         movies_data = JSONParser().parse(request)
#         movies_serializer = MovieSerializer(data = movies_data)
#         if movies_serializer.is_valid():
#             movies_serializer.save()
#             return JsonResponse("Added Successfully",safe = False)
#         return JsonResponse("Failed to Add",safe = False)
#     elif request.method=='PUT':
#         movie_data=JSONParser().parse(request)
#         movie= Movie.objects.get(MovieId = movie_data['MovieId'])
#         movies_serializer=MovieSerializer(movie, data = movie_data)
#         if movies_serializer.is_valid():
#             movies_serializer.save()
#             return JsonResponse("Updated Successfully", safe = False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         movie=Movie.objects.get(MovieId = id)
#         movie.delete()
#         return JsonResponse("Deleted Successfully",safe = False)
