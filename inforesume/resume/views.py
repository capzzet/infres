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
        {'title': "Блог", 'url_name': 'blog'}, ]
def index(request):
    context = {
        'menu':menu
    }
    return render(request, 'resume/html/index.html')

def resume(request):
    return render(request, 'resume/html/resume.html')