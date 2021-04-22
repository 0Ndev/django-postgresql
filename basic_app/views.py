from django.shortcuts import render, get_object_or_404
from .models import Cheatsheet


def index(req):
    return render(req, 'index.html')


def cheatsheets(req):
    cheatsheets = Cheatsheet.objects
    # print("cheatsheets:", cheatsheets)
    return render(req, 'cheatsheets.html', {'cheatsheets': cheatsheets})


def cheatsheet(req, article_id):
    cheatsheet = get_object_or_404(Cheatsheet, pk=article_id)
    # print("cheatsheet:", cheatsheet)
    return render(req, 'sheet.html', {'cheatsheet': cheatsheet})


# def cheatsheet_view(req):
#     return render(req, 'cheatsheet_view.html')
