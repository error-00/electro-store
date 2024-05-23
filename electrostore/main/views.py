from django.shortcuts import render


def index(request):
    context = {
        "title": "Electro - HTML Ecommerce Template",
    }
    return render(request, "main/index.html", context)
