from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:pk>", views.ListingPage.as_view(), name="listing"),
    path("listing/create", views.CreateListingView.as_view(), name="listing-create"),
    path("category-create", views.CreateCategoryView.as_view(), name="category-create"),
]
