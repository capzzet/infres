from django.http import HttpResponse
from django.shortcuts import render, redirect
from docxtpl import DocxTemplate
import os
import mimetypes
import pythoncom
from docx2pdf import convert
from pathlib import Path
# Create your views here.
menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Резюме", 'url_name': 'resume'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Блог", 'url_name': 'blog'},
        {'title': "Контакты", 'url_name': 'contacts'}, ]
def index(request):
    context = {
        'menu':menu,
        'intro_under':[{'data_scroll':'#about','under_text':'Что такое конструктор',},
                       {'data_scroll':'#benefits','under_text':'Преимущества',},
                       {'data_scroll':'#creation','under_text':'Процесс создания',},
                       {'data_scroll':'#footer','under_text':'Связаться',},],
    }
    return render(request, 'resume/html/index.html',context)
def about(request):
    context = {
        'menu': menu
    }
    return render(request, 'resume/html/about.html',context)

def blog(request):
    context = {
        'menu': menu
    }
    return render(request, 'resume/html/blog.html',context)

def contacts(request):
    context = {
        'menu': menu
    }
    return render(request, 'resume/html/contacts.html',context)
def resume(request):
    context = {
        'menu': menu
    }
    return render(request, 'resume/html/resume.html',context)

def custom_page_not_found_view(request, exception):
    return render(request, "resume/errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "resume/errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "resume/errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "resume/errors/400.html", {})