from django.shortcuts import render, get_object_or_404
from .forms import toish
from .models import ish
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def create(request):
    form = toish(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)
def asosiy(request):
    return render(request, 'asosiy.html')
def list(request):
    list = ish.objects.all()
    context2 = {
        'list': list
    }
    return render(request, 'list.html', context2)
def korish(request, nomi):
    get = get_object_or_404(ish, nomi=nomi)
    context3 = {
        'get': get
    }
    return render(request, 'korish.html', context3)
class delete(DeleteView):
    model = ish
    template_name = 'uchirish.html'
    success_url = reverse_lazy("list")

