from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


@login_required
def dashboard(request):
    return render(request, 'gontend/gontend.html')


def status(request):
    return HttpResponse()
