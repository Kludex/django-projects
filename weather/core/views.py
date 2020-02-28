from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from weather.settings import WEATHER_API_KEY

import requests

from .models import City
from .forms import CityForm


class CityCreateView(CreateView):
    model = City
    template_name = 'core/cities.html'
    form_class = CityForm
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api}'
        cities = City.objects.all()
        info = []

        for city in cities:
            context_city = {}
            r = requests.get(url.format(city=city,
                                        unit='metric',
                                        api=WEATHER_API_KEY)).json()
            context_city['name'] = city.name
            context_city['temperature'] = r['main']['temp']
            context_city['description'] = r['weather'][0]['description']
            context_city['icon'] = r['weather'][0]['icon']
            context_city['pk'] = city.pk
            info.append(context_city)
        context['cities'] = info
        return context

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
        return redirect(reverse('core'))

class CityDeleteView(DeleteView):
    model = City

    def get_success_url(self):
        return reverse('core')
