from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Apartments


def index(request):
    apartments = Apartments.objects.order_by(
        "-list_date").filter(is_publish=True)

    paginator = Paginator(apartments, 5)
    page = request.GET.get('page')
    pagged_apartments = paginator.get_page(page)
    context = {
        'apartments': pagged_apartments
    }
    return render(request, "pages/apartments.html", context)


def apartment(request, apartment_id):
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    context = {
        "apartment": apartment
    }
    return render(request, 'pages/apartment.html', context)


def search(request):
    estate_list = Apartments.objects.order_by(
        "-list_date").filter(is_publish=True)

    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            estate_list = estate_list.filter(city__iexact=city)

    print(estate_list)
    context = {
        'estate_list': estate_list
    }
    return render(request, 'pages/search.html', context)



def favorite(request):
    if request.method == 'POST':
        apartment_id = request.POST['apartment_id']
        apartment = Apartments.objects.filter(id=apartment_id)
        fav = Apartments(request.user)
        favorite_apartment = apartment.filter(is_favorite=False).update(is_favorite=True)

    return redirect('estatelist')

