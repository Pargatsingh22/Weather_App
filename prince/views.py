from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    city = request.GET.get('city', "lucknow")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cb0530d7a9e4f4ce94e8a6860197a2ea'
    data = requests.get(url).json()
    
    payload = {
        'city' : data['name'],
        'weather': data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelven_temperature': data['main']['temp'],
        'celcius_temperature': int(data['main']['temp'] - 273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    } 
    
    context = {'data' : payload}
    print(context)
    
    
    
    
    
    return render(request, 'home.html', context)