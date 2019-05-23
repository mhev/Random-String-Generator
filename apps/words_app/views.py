from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    count = 0
    if 'counter' in request.session:
        count = request.session['counter']

    count += 1

    request.session['counter'] = count

    context = {
        "theword": get_random_string(length=14),
    }

    return render(request, 'words_app/index.html', context)

def reset(request):
    del request.session['counter']

    return redirect('/')