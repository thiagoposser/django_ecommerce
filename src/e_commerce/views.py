# from django.http import HttpResponse
# from django.shortcuts import render
# def home(request):
#     return render(request, "home.html", {})

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    if request.method == "POST":
        print(request.POST)
    return render(request, "contact/view.html", context)

