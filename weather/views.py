import  requests
from django.shortcuts import render, HttpResponse, redirect
from weather.models import location
from weather.forms import CityForm
from django.contrib import messages

# Create your views here.
def index(request):

    url = ' http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=23f5e3d47093431ffabf3d7a5fb65fa9'
    if request.method == "POST":
            form = CityForm(request.POST)
            if form.is_valid():
                c = form.cleaned_data['name']
                count = location.objects.filter(name = c).count()
                if count == 0:
                    r = requests.get(url.format(c)).json()
                    if r['count'] != 0:
                        form.save()
                        messages.success(request, "City Added Sucessfully")
                    else:
                        messages.error(request, "City doesnot exists")
                        return redirect('base')

                else:
                    messages.error(request, "City already present")
                    return redirect('base')
    form = CityForm()
    a = location.objects.all()
    b = []
    for city in a:
        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city.name,
            'temperature' : r['list'][0]['main']['temp'],
            'description' : r['list'][0]['weather'][0]['description'],
            'icon' : r['list'][0]['weather'][0]['icon']
        }
        b.append(weather)
    context = {'b' : b , 'form':form}
    return render(request ,'base.html',context)





def remove_city(request, name):
    try:
        a = location.objects.get(name = name).delete()
        messages.success(request, "Removed Sucessfully")
        return redirect('base')
    except:
        messages.error(request , "Cannot be removed")
        return redirect('base')

