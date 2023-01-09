from django.shortcuts import render
from .models import PhaseOne
from django.http import JsonResponse
# Create your views here.
def home(req):
    return render(req, 'index.html')

def start_phase1(req):
    t = req.GET.get('target')
    n = req.GET.get('name')
    m = req.GET.get('mobile')
    PhaseOne.objects.create(target=t, name=n, mobile=m)
    return JsonResponse({'status': f'Created {n}'})