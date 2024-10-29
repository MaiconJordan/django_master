from django.shortcuts import render
from django.shortcuts import render
from cars.models import Car
# Create your views here.



def car_view(request):
    print(request.GET.get('search'))
    
    cars = Car.objects.filter(brand = 1)
    
    return render(request, 'cars.html',
                  {'cars' :cars})