from django.shortcuts import render
from django.http import  HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')
# Create your views here.
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if(request.GET.get('Uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if (request.GET.get('special character')):
            characters.extend(list('!@*&%$'))

    if (request.GET.get('Number')):
            characters.extend(list('123456789'))

    length = int(request.GET.get('length',11))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

