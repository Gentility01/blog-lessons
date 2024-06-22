from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {}
    return render(request, "core/index.html", context)


def aboutpage(request):
    context = {}
    return render(request, "core/about.html", context)