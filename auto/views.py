from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.views.generic import ListView, DetailView, CreateView


class CarList(ListView):
    model = Car
    template_name = "index.html"


def car_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('/')
    else:
        form = CarForm
        return render(request, 'car_create_form.html', {'form': form})


class SearchResult(ListView):
    model = Car
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Car.objects.filter(
            Q(car_brand__icontains=query)
            | Q(model__icontains=query)
            | Q(year_of_issue__icontains=query)
            | Q(gear_box__icontains=query)
            | Q(color__icontains=query)
        )
        return object_list
