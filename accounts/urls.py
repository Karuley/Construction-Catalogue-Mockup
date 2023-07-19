from django.urls import path
from . import views
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),

    path('catalogue', views.catalogue, name="catalogue"),
    path('comp_catalogue', views.comp_catalogue, name="comp_catalogue"),
    path('contacts', views.contacts_page, name="contacts"),

    path('products/<str:pk>/', views.products, name="products"),
    path('company/<str:pk>/', views.company, name="company"),
    path('company_guest/<str:pk>', views.company_guest, name="company_guest"),
    path('company_form/<str:pk>', views.company_form, name="company_form"),


    path('product_form/<str:pk>/', views.create_products, name="product_form"),
    #path('single_product_form/<str:pk>/', views.create_product, name="single_product_form"),
    path('update_product/<str:pk>/', views.update_product, name="update_product"),
    path('delete_product/<str:pk>/', views.delete_product, name="delete_product"),

    path('login', views.loginPage, name="login"),
    path('register', views.registerPage, name="register"),
    path('logout', views.logoutUser, name="logout"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)