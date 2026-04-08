from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с необходимыми правами'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        content_type = ContentType.objects.get_for_model(Product)

        can_unpublish = Permission.objects.get(codename='can_unpublish_product', content_type=content_type)
        delete_product = Permission.objects.get(codename='delete_product', content_type=content_type)

        group.permissions.add(can_unpublish, delete_product)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Группа "{group.name}" успешно создана'))
        else:
            self.stdout.write(self.style.WARNING(f'Группа "{group.name}" была создана'))
