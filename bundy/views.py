from django.shortcuts import render  # Chyběl import render!
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Jacket
from .forms import JacketForm
import os
from django.conf import settings

def check_images(request):
    image_dir = os.path.join(settings.BASE_DIR, 'bundy', 'static', 'bundy')
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return render(request, 'bundy/check_images.html', {'image_files': image_files})

class JacketCreateView(CreateView):
    model = Jacket
    form_class = JacketForm
    template_name = 'bundy/vytvor.html'
    success_url = reverse_lazy('jacket-list')  # Přesměrování na seznam bund

def menu(request):
    return render(request, 'bundy/base.html')

def sklad(request):
    return render(request, 'bundy/sklad.html')

def vytvor(request):
    return render(request, 'bundy/vytvor.html')



def home(request):
    return render(request, 'bundy/base.html')


class JacketListView(ListView):
    model = Jacket
    template_name = 'bundy/sklad.html'  # Změněno z 'bundy/jacket_list.html'
    context_object_name = 'jackets'
