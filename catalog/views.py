from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {
        'title': 'Главная страница',
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = super().get_queryset().order_by('-created_at', 'pk')[:5]
        else:
            queryset = super().get_queryset().filter(
            )
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = Version.objects.filter(product=product, version_indication=True).last()
            if active_version:
                product.active_version_number = active_version.version_num
                product.active_version_name = active_version.version_name
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Товар',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        active_version = Version.objects.filter(product=self.object, version_indication=True).last()
        if active_version:
            context['active_version_number'] = active_version.version_num
            context['active_version_name'] = active_version.version_name
        else:
            context['active_version_number'] = None
            context['active_version_name'] = None

        return context


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


class CreateProductView(LoginRequiredMixin, CreateView):
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


class UpdateProductView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    permission_required = 'catalog.change_product'
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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            return redirect(reverse('catalog:home'))
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data




class DeleteProductView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:home')
