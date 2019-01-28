from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def cars_list(request):
    years = []
    for car in Car.objects.all():
        years.append({
            'id': car.id,
            'year': car.year
        })
    from_year = request.GET.get('from_year', '')
    to_year = request.GET.get('to_year', '')
    order_by = request.GET.get('order_by', '')
    if from_year and to_year:
        cars_list = Car.objects.filter(year__range=(from_year, to_year))
    elif from_year:
        cars_list = Car.objects.filter(year__range=(from_year, '2019'))
    elif to_year:
        cars_list = Car.objects.filter(year__range=('0', to_year))
    elif order_by:
        cars_list = Car.objects.all()
        if order_by in ('first_name', 'year', 'price'):
            cars_list = cars_list.order_by(order_by)
            if request.GET.get('reverse', '') == '1':
                cars_list = cars_list.reverse()
    else:
        cars_list = Car.objects.all()

    paginator = Paginator(cars_list, 10)
    page = request.GET.get('page', 1)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'cars': cars,'years':years})

def car_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.author = request.user
            car.published_date = timezone.now()
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = PostForm()
    return render(request, 'blog/car_edit.html', {'form': form})

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.author = request.user
            car.published_date = timezone.now()
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = PostForm(instance=car)
    return render(request, 'blog/car_edit.html', {'form': form})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'blog/car.html', {'car': car})

def car_del(request, pk):
    obj = Car.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect("/")

