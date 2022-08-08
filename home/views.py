from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


# def index(request):
#     return HttpResponse('''<a href='/'>Home</a> <br>
#     <a href='/removepunc'>removepunc</a> <br>
#     <a href='/capitalizefirst'>capitalizefirst</a> <br>
#     <a href='/newlineremove'>newlineremove</a> <br>
#     <a href='/spaceremove'>spaceremove</a> <br>
#     <a href='/charcount'>charcount</a> <br>
#     ''')

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations',
                  'analyzed_text': analyzed,
                  }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase',
                  'analyzed_text': analyzed,
                  }
        djtext = analyzed

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new line',
                  'analyzed_text': analyzed,
                  }
        djtext = analyzed

    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space',
                  'analyzed_text': analyzed,
                  }
        djtext = analyzed

    if charcount == "on":
        analyzed = ""
        charno = 0
        for char in djtext:
            if char != " ":
                charno += 1
            analyzed = f"Char count is {charno}"
        params = {'purpose': 'Removed Extra Space',
                  'analyzed_text': analyzed,
                  }
        djtext = analyzed

    if(removepunc != 'on' and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on"):
        return HttpResponse("Please select the operation to be performed")

    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")
