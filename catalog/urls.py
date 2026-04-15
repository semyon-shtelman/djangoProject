from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_edit"
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path("contacts/", views.ContactsTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/unpublish/", views.UnpublishProductView.as_view(), name="product_unpublish"),
    path("category/", views.CategoryListViews.as_view(), name="category"),
    path('category/<int:category_id>/', views.CategoryProductsView.as_view(), name='category_products')
]
