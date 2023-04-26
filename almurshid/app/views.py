import json

from django.http import HttpResponse
from django.shortcuts import render

from .forms import MessageForm
from .models import About, Book, Message, News, Social, Wish


def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Your Message successfully recieved",
            }
        else:
            message = repr(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": message,
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        wishes = Wish.objects.filter(is_active=True)
        books = Book.objects.filter(is_active=True)
        messages = Message.objects.filter(is_active=True)
        newses = News.objects.filter(is_active=True)
        socials = Social.objects.filter(is_active=True)
        about = About.objects.first()
        context = {
            "is_index": True,
            "wishes": wishes,
            "books": books,
            "messages": messages,
            "newses": newses,
            "socials": socials,
            "about": about,
            "form": MessageForm(),
        }
        return render(request, "app/index.html", context)


def read_online(request):
    about = About.objects.first()
    context = {"is_read_online": True, "about": about}
    return render(request, "app/read_online.html", context)


def read_book(request, id):
    book = Book.objects.get(id=id)
    context = {"is_read_book": True, "book": book}
    return render(request, "app/read_book.html", context)
