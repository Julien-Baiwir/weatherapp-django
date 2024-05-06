from django.shortcuts import render
import json
import urllib.request

def index(request):
    city = ''
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city', '')
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=c29a355949954abe9d576d08246566b1').read()
        json_data = json.loads(res)
        if 'sys' in json_data and 'main' in json_data and 'coord' in json_data:
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
    return render(request, 'index.html', {'city': city, 'data': data})

