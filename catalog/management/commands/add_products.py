from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog/fixtures/categories_fixture.json")
        call_command("loaddata", "catalog/fixtures/products_fixture.json")

        self.stdout.write(
            self.style.SUCCESS(f"loaded categories {Category.objects.count()}")
        )
        self.stdout.write(
            self.style.SUCCESS(f"loaded products {Product.objects.count()}")
        )
