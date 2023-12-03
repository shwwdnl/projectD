from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        categories = ['Книги', 'Смартфоны']
        for name in categories:
            category = Category(name=name)
            category.save()

        products = [
            ('Harry Potter', 'A fantasy novel series', 'Книги', 500),
            ('iPhone 12', 'A smartphone with a 6.1-inch display', 'Смартфоны', 80000),

        ]
        for name, description, category_name, price in products:
            category = Category.objects.get(name=category_name)
            product = Product(name=name, description=description, category=category, price=price, owner=f'User')
            product.save()
