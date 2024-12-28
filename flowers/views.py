from django.shortcuts import render, get_object_or_404
from .models import Flower, Type

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/flower_list.html', {'flowers': flowers})

def flower_detail(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})

def flowers_by_type(request, type_id):
    flowers = Flower.objects.filter(type_id=type_id)
    return render(request, 'flowers/flower_by_type.html', {'flowers': flowers})

def type_list(request):
    types = Type.objects.all()
    return render(request, 'types/type_list.html', {'types': types})