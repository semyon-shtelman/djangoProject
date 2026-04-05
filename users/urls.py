from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.CustomRegisterView.as_view(), name="register"),
    path(
        "user/profile/<int:pk>/edit/",
        views.ProfileUpdateView.as_view(),
        name="profile_edit",
    ),
    path("user/<int:pk>/profile/", views.ProfileDetailView.as_view(), name="profile"),
]
