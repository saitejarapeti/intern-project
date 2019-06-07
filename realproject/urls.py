from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from ecommerce import views
from django.conf.urls import include, url
from ecommerce.views import HomeView,ItemDetailView,add_to_cart,OrderSummaryView,remove_single_item_from_cart,CheckoutView
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    #path('register/', views.register),
    #path('', views.home),
    path('home', HomeView.as_view()),
    #path('base', views.base),
    path('order-summary/', OrderSummaryView.as_view(),name = 'order-summary'),
    path('checkout', CheckoutView.as_view(),name='checkout'),
    path('products/<slug>/', ItemDetailView.as_view(), name='core'),
    path('add-to-cart/<slug>/',views.add_to_cart,name = "add-to-cart"),
    path('remove-from-cart/<slug>/',views.remove_from_cart,name = "remove-from-cart"),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart, name="remove-single-item-from-cart"),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)