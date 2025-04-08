from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Wilaya, Etablissement

# Etablissement

class WilayaView(DetailView):
    model = Wilaya

class WilayaCreate(CreateView):
    model = Wilaya
    fields = '__all__'

class WilayaUpdate(UpdateView):
    model = Wilaya
    fields = '__all__'

class WilayaDelete(DeleteView):
    model = Wilaya
    success_url = reverse_lazy('wilaya-list-view')

class WilayaList(ListView):
    model = Wilaya

# Etablissement
class EtablissementView(DetailView):
    model = Etablissement

class EtablissementCreate(CreateView):
    model = Etablissement
    fields = '__all__'

class EtablissementUpdate(UpdateView):
    model = Etablissement
    fields = '__all__'

class EtablissementDelete(DeleteView):
    model = Etablissement
    success_url = reverse_lazy('etablissement-list-view')

class EtablissementList(ListView):
    model = Etablissement

# Centre Exam

# Exam

def index(request):
    return render(request, 'index.html', {})
    #return HttpResponse("Hello, world. You're at the rimbac app!")