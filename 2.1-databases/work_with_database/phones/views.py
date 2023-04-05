from .models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort_order_param = request.GET.get('sort', 'name')

    Phone.objects.all()
    if sort_order_param == 'name':
        sort_order ='name'
    elif sort_order_param == 'min_price':
        sort_order ='price'
    else:
        sort_order ='-price'

    phone_objects = Phone.objects.order_by(sort_order)

    template = 'catalog.html'
    context = {
        'phones': phone_objects,
    }
    return render(request, template, context)



def show_product(request, slug):
    phone_product = Phone.objects.filter(slug=slug)

    phones_list = list(phone_product)

    phone = {
        "name": phones_list[0].name,
        "price": phones_list[0].price,
        "image": phones_list[0].image_url,
        "release_date": phones_list[0].release_date,
        "lte_exist": phones_list[0].lte_exist,
        "slug": phones_list[0].slug
    }

    template = 'product.html'
    context = { "phone": phone }
    print(context)

    return render(request, template, context)