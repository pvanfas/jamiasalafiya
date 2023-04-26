import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ResultForm
from .models import Result


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)


def result(request):
    form = ResultForm()
    choice = request.GET.get("choice", None)
    if choice:
        result = Result.objects.get(pk=choice)
    else:
        result = None
    context = {"is_result": True, "form": form, "result": result}
    return render(request, "web/result.html", context)
