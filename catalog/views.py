from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная страница',
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Товар',
    }


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты',
    }

    def contacts(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(f'{name} ({email}): {message}')
        return render(request, 'catalog/contacts.html', self.extra_context)
