from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def index(request):
  ppl = Pessoa.objects.all()
  ctx = {
    'ppl_list': ppl,
  }
  return render(request, 'index.html', ctx)