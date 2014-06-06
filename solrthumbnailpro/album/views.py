from django.views.generic import ListView
from .models import Foto

class HomeListView(ListView):

    template_name = 'home.html'
    model = Foto
    context_object_name = 'fotos'