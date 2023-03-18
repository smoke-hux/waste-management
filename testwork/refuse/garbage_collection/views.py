from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import GarbageCollection

def garbage_collection(request):
    collections = GarbageCollection.objects.filter(user=request.user)
    total_earnings = sum(c.earnings for c in collections)
    organic_earnings = sum(c.earnings for c in collections if c.type == 'organic')
    inorganic_earnings = sum(c.earnings for c in collections if c.type == 'inorganic')
    return render(request, 'garbage_collection.html', {'collections': collections, 'total_earnings': total_earnings, 'organic_earnings': organic_earnings, 'inorganic_earnings': inorganic_earnings})
