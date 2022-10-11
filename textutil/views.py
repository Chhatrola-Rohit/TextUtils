# I have created this file - Rohit 
import http
import re
from ssl import HAS_TLSv1_1
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text 
    djtext=request.GET.get('text','default')
    # check checkbox value 
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremove=request.GET.get('newlineremove','off')
    extraspaceremove=request.GET.get('extraspaceremove','off')
    charcount=request.GET.get('charcount','off')

    # Analze the text
    if removepunc=="on":
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for  char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'Removed punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()

        params={'purpose':'Capitalize Text', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)


    if(extraspaceremove=="on"):
        analyzed=""
        for index , char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed= analyzed+ char

        params={'purpose':'Extra space Remove', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(newlineremove=="on"):
        analyzed=""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed= analyzed + char

        params={'purpose':'Remove new line', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(charcount=="on"):
        count=0
        for char in djtext:
            if char!=" ":
                count= count+ 1
        analyzed=djtext +"--->"+ str(count)
        params={'purpose':'Character Count', 'analyzed_text':analyzed}
        # djtext=analyzed
        # return render(request,'analyze.html',params)
        
    if(removepunc != "on" and newlineremove!="on" and extraspaceremove!="on" and fullcaps!="on" and charcount!="on"):
        params={'purpose':'Not select any operation', 'analyzed_text':djtext}
        return render(request,'error.html',params)

    return render(request, 'analyze.html', params)
