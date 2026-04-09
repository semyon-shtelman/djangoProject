from functools import update_wrapper
from itertools import product

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.filter(is_publish=True)

        if user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()

        published_product = Product.objects.filter(is_publish=True)
        my_product = Product.objects.filter(owner=user)

        return published_product.union(my_product)


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_object(self):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        user = self.request.user

        if user.has_perm('catalog.can_unpublish_product'):
            return product

        if user == product.owner:
            return product

        if product.is_publish:
            return product

        raise Http404("Продукт не найден или недоступен")

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def test_func(self):
        product = self.get_object()
        user = self.request.user

        return user == product.owner


    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        product = self.get_object()
        user = self.request.user

        if user.has_perm('catalog.can_unpublish_product'):
            return True

        if user.has_perm('catalog.delete_product'):
            return True

        return user == product.owner

class UnpublishProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)


        product.is_publish = not product.is_publish
        product.save()

        return redirect('catalog:product_detail', pk=product.pk)


class ContactsTemplateView(generic.TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
