from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    phones = Phone.objects.all()
    if sort == 'cheap':
        phones = phones.order_by('price')
    elif sort == 'expensive':
        phones = phones.order_by('-price')
    elif sort == 'name':
        phones = phones.order_by('name')

    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        "phone": Phone.objects.filter(slug=slug).first()
    }
    return render(request, template, context)
