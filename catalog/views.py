from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
