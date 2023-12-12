from django.contrib import admin
from pytils.translit import slugify

from blog.models import Blog


# Register your models here.


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'date_create', 'view_count',)
    search_fields = ('title', 'body',)
    list_filter = ('date_create',)

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)