# I have created this file - Raj
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    data = request.POST.get('text', 'default')

    # check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount','off')

    # check which check box is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\/,.@#$%~^&*<>?-`'''
        analyzed = ""
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text' : analyzed}
        data = analyzed

    if fullcaps == 'on':
        analyzed = ''
        for char in data:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Upper Case' , 'analyzed_text': analyzed}
        data = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in data:
            if char != '\n'and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        data = analyzed

    if extraspaceremover =='on':
        analyzed = ''
        for index, char in enumerate(data):
            if not(data[index] == ' ' and data[index + 1] == ' '):
                analyzed = analyzed + char

        params = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed}
        data = analyzed

    if charcount == 'on':
        analyzed = 0
        for char in data:
            if char != ' ':
                analyzed = analyzed + 1
        strings = data + '\n\n\nThe count of character is ' + str(analyzed)
        params ={'purpose':'Char Count ', 'analyzed_text': strings}
    if(removepunc != 'on' and fullcaps !='on' and newlineremover != 'on'and extraspaceremover !='on' and charcount != 'on'):
        return HttpResponse("Please select any operation to see the result <br><a href = http://127.0.0.1:8000/>Home</a>")
    return render(request, 'analyze.html', params)






