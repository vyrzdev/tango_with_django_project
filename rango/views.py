from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rango.models import Category, Page


def index(request: HttpRequest):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
        'pages': page_list
    }

    return render(request, 'rango/index.html', context=context_dict)


def about(request: HttpRequest):
    context_dict = {'boldmessage': 'This tutorial has been put together by Ben.'}

    return render(request, 'rango/about.html', context=context_dict)


def show_category(request: HttpRequest, category_name_slug: str):
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict = {
            "pages": pages,
            "category": category
        }

    except Category.DoesNotExist:
        context_dict = {
            "category": None,
            "pages": None
        }

    return render(request, 'rango/category.html', context=context_dict)
