from django.shortcuts import render
from .models import Slider, Settings


def home(request):
    sliders = Slider.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'sliders':sliders,
        'settings':settings,
    }
    return render(request, 'index.html', context)