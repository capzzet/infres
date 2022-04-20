from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Резюме", 'url_name': 'resume'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Блог", 'url_name': 'blog'}, ]
def index(request):
    context = {
        'menu':menu
    }
    return render(request, 'resume/html/index.html')