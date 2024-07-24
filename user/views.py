from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = "user/index.html"
