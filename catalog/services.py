from .models import Product, Category


class ProductService:
    @staticmethod
    def get_product_by_category(category_id):
        return Product.objects.filter(category=category_id)
