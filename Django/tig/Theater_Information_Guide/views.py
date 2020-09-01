from django.shortcuts import render, get_object_or_404
from Theater_Information_Guide.models import TheatersDetails
from django.http import JsonResponse
from django.db.models import Q


def index(request):
    theaters_data = TheatersDetails.objects.select_related().all()[:6]
    context = {
        'theaters_data': theaters_data
    }
    return render(request, "index.html", context)


def theaters_index(request):
    theaters_data = TheatersDetails.objects.select_related().all()[:6]
    context = {
        'theaters_data': theaters_data
    }
    return render(request, "theaters_index.html", context)


def theaters_detail(request, pk):
    theaters_data = get_object_or_404(TheatersDetails, pk=pk)
    context = {
        'theaters_data': theaters_data
    }
    return render(request, "theater_detail.html", context)


def developer(request):
    context = {

    }
    return render(request, "developer.html", context)


def change_option(request):
    option = request.GET['option']

    if option == 'popular-order':
        theaters_data = TheatersDetails.objects.select_related().all()[:6]
    elif option == 'latest-order':
        theaters_data = TheatersDetails.objects.select_related().all().order_by('-theaterid__openingday')[:6]
    elif option == 'name-order':
        theaters_data = TheatersDetails.objects.select_related().all().order_by('theaterid__theatername')[:6]

    data = []
    for i in theaters_data:
        data_dict = dict()
        data_dict['id'] = i.theaterid.theaterid
        data_dict['name'] = i.theaterid.theatername
        data_dict['price'] = i.price
        data_dict['period'] = i.theaterid.period
        data_dict['place'] = i.theaterid.place
        data_dict['image'] = i.image
        data.append(data_dict)

    context = {
        'theater_data': data
    }
    return JsonResponse(context)


def change_page(request):
    page = request.GET['page']
    option = request.GET['option']

    if option == 'popular-order':
        theaters_data = TheatersDetails.objects.select_related().all()
        if page == 'page-01':
            theaters_data = theaters_data[:6]
        elif page == 'page-02':
            theaters_data = theaters_data[6:12]
        elif page == 'page-03':
            theaters_data = theaters_data[12:16]
    elif option == 'latest-order':
        theaters_data = TheatersDetails.objects.select_related().all().order_by('-theaterid__openingday')
        if page == 'page-01':
            theaters_data = theaters_data[:6]
        elif page == 'page-02':
            theaters_data = theaters_data[6:12]
        elif page == 'page-03':
            theaters_data = theaters_data[12:16]
    elif option == 'name-order':
        theaters_data = TheatersDetails.objects.select_related().all().order_by('theaterid__theatername')
        if page == 'page-01':
            theaters_data = theaters_data[:6]
        elif page == 'page-02':
            theaters_data = theaters_data[6:12]
        elif page == 'page-03':
            theaters_data = theaters_data[12:16]

    data = []
    for i in theaters_data:
        data_dict = dict()
        data_dict['id'] = i.theaterid.theaterid
        data_dict['name'] = i.theaterid.theatername
        data_dict['price'] = i.price
        data_dict['period'] = i.theaterid.period
        data_dict['place'] = i.theaterid.place
        data_dict['image'] = i.image
        data.append(data_dict)

    context = {
        'theater_data': data
    }
    return JsonResponse(context)


def search(request):
    user_input = request.GET['user_input']
    location = request.GET['location']
    type = request.GET['type']

    theaters_data = TheatersDetails.objects.select_related().all()

    theaters_data = theaters_data.filter(
        Q(theaterid__theatername__icontains=user_input) &
        Q(theaterid__location__icontains=location) &
        Q(theaterid__openrun__icontains=type)
    )

    search_data = []
    for i in theaters_data:
        data_dict = dict()
        data_dict['id'] = i.theaterid.theaterid
        data_dict['name'] = i.theaterid.theatername
        data_dict['price'] = i.price
        data_dict['period'] = i.theaterid.period
        data_dict['place'] = i.theaterid.place
        data_dict['image'] = i.image
        search_data.append(data_dict)
    context = {
        'search_data': search_data
    }
    return render(request, "search.html", context)
