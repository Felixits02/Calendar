from django.http import HttpResponse
from django.shortcuts import render
import calendar


def home(request):
   yy = 2026
   mm = 11
   cal = calendar.month(yy, mm)
   
   return render(request, 'home.html', {'cal': cal})