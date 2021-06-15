from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView,FormView)
from .models import Standard, Courses, Lesson

class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'colleges/standard_list_view.html'





