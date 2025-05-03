from django.shortcuts import render
from django.http import JsonResponse
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return JsonResponse(
        {"All movies": "http://localhost:8000/api/v1/movies/"},
        )

@api_view(['POST'])
def create_movie(request):
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def all_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['PUT'])
def update_movie(request, id):
    if request.method == 'PUT':
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_movie(request, id):
    if request.method == 'DELETE':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return JsonResponse({'message': 'Movie deleted successfully'}, status=204)