from django.shortcuts import render
from .models import *

def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, "btest/index.html", {'bbs': bbs})

