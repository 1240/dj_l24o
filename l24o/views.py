from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from l24o.models import Serial


class serials_list_view(ListView):
    template_name = 'serial_list.html'
    model = Serial

