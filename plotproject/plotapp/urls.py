from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.HomeView.as_view(), name="home"),
                  path('listing/', views.ListView.as_view(), name="listing"),
                  path('appartements/', views.Appartements.as_view(), name="appartements"),
                  path('appartementslisting/', views.AppartementsListing.as_view(), name='appartementslisting'),
                  path('food&life/', views.FoodAndlife.as_view(), name="food&life"),
                  path('food&lifelisting/', views.FoodAndLifeListing.as_view(), name="food&lifelisting"),
                  path('cars/', views.Cars.as_view(), name="cars"),
                  path('carslisting/', views.CarsListing.as_view(), name="carslisting"),
                  path('shopping/', views.Shopping.as_view(), name="shopping"),
                  path('shoppinglisting/', views.ShoppingListing.as_view(), name="shoppinglisting"),
                  path('travelling/', views.Travelling.as_view(), name="travelling"),
                  path('travellinglisting/', views.TravellingListing.as_view(), name="travellinglisting"),
                  path('mylisting/', views.MylistingsView.as_view(), name="mylisting"),
                  path('ContactForm/', views.ContactFormView.as_view(), name="ContactForm"),
                  path('search/', views.SearchView.as_view(), name="search"),
                  path('reviews/',views.Review.as_view(),name="reviews"),
                  path('privacypolicy/',views.PrivacyPolicy.as_view(),name="privacypolicy"),
                  path('aboutus/', views.AboutUs.as_view(), name="aboutus"),
                  path('usefulsites/', views.UsefulSites.as_view(), name="usefulsites"),
                  path('awards/', views.Awards.as_view(), name="awards"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)