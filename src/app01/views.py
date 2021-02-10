from django.shortcuts import render


def main(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'main.html')