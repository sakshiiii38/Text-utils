# I have Created this file - Sakshi

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def analyze(request):
    djtext = request.POST.get('text', 'off')

    removepunc = request.POST.get('removepunc', 'off')

    fullcaps = request.POST.get('fullcaps', 'off')

    RemoveNewLine = request.POST.get('RemoveNewLine', 'off')

    print(removepunc)

    print(djtext)

    if removepunc == 'on':
        punctuations = ''';,!~.[$@^&*()}{|\/]-_+=~` ?><'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'capatilize the sentence', 'analyzed_text': analyzed}
        djtext = analyzed

    if RemoveNewLine == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char.upper()

        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}

    if(removepunc!='on' and RemoveNewLine!='on' and fullcaps!='on'):
        return HttpResponse("ERROR")
    return render(request, 'analyze.html', params)


