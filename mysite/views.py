from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "home.html"


def about(request):
    context = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return render(request, 'about.html', context)
