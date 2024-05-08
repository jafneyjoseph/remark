from django.shortcuts import render
from movie.models import Movie
from django.db.models import Q

def searchResult(request):
    results = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        results = Movie.objects.filter(title__icontains=query)
    return render(request, 'Search.html', {'query': query, 'results': results})
