from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': pages_list}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'page_author': "matonsjojec"}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        #retrieve pages associated with category (if none, returns empty list); add list to context_dict
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        #add category to context_dict
        context_dict['category'] = category
    except Category.DoesNotExist:
        # don't to anything if can't find the category; template shows "no category" message.
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
