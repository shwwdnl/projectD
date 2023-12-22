from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
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


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Добавить товар',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version_form'] = VersionForm()
        return context

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.owner = self.request.user
            self.object.save()
        return super().form_valid(form)


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Изменить товар',
    }

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.owner = self.request.user
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail_product', args=[self.object.pk])


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
