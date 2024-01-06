from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from django.db.models import Q
from .models import MyListing
from .forms import MyListingsForm, ContactUsForm


class LoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class HomeView(ListView):
    template_name = "home.html"
    model = MyListing
    context_object_name = 'listings'


class ListView(LoginRequiredMixin, ListView):
    template_name = "listing.html"
    model = MyListing
    context_object_name = 'appartementslistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='appartements')


class Appartements(ListView):
    template_name = 'appartements.html'
    model = MyListing
    context_object_name = 'appartementslistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='appartements')


class AppartementsListing(ListView):
    template_name = 'appartements1.html'
    model = MyListing
    context_object_name = 'appartementslistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='appartements')


class FoodAndlife(ListView):
    template_name = "food&life.html"
    model = MyListing
    context_object_name = 'foodandlifelistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='foodandlife')


class FoodAndLifeListing(ListView):
    template_name = "food&lifedy.html"
    model = MyListing
    context_object_name = 'foodandlifelistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='foodandlife')


class Cars(ListView):
    template_name = "cars.html"
    model = MyListing
    context_object_name = 'carlistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='car')


class CarsListing(ListView):
    template_name = "carsdy.html"
    model = MyListing
    context_object_name = 'carlistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='car')


class Shopping(ListView):
    template_name = "shopping.html"
    model = MyListing
    context_object_name = 'shoppinglistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='shopping')


class ShoppingListing(ListView):
    template_name = "shoppingdy.html"
    model = MyListing
    context_object_name = 'shoppinglistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='shopping')


class Travelling(ListView):
    template_name = "travelling.html"
    model = MyListing
    context_object_name = 'travellinglistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='travelling')


class TravellingListing(ListView):
    template_name = "travellingdy.html"
    model = MyListing
    context_object_name = 'travellinglistings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='travelling')


class MylistingsView(LoginRequiredMixin, FormView):
    template_name = "mylistings.html"
    form_class = MyListingsForm
    success_url = "/ContactForm/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SearchView(ListView):
    template_name = 'search.html'
    model = MyListing
    context_object_name = 'listings'

    def get_queryset(self):
        query = self.request.GET.get('q')
        address = self.request.GET.get('address')
        price_range = self.request.GET.get('price')

        queryset = self.model.objects.all()

        if query:
            queryset = queryset.filter(Q(area__icontains=query))

        if address:
            queryset = queryset.filter(Q(location__icontains=address))

        if price_range:
            if price_range == "1000+":
                queryset = queryset.filter(Q(price__gte=1000))
            else:
                min_price, max_price = price_range.split('-')
                queryset = queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

        return queryset


class Review(TemplateView):
    template_name = 'review.html'


class PrivacyPolicy(TemplateView):
    template_name = 'privacypolicy.html'


class AboutUs(TemplateView):
    template_name = 'about.html'


class UsefulSites(TemplateView):
    template_name = 'usefulsites.html'


class Awards(TemplateView):
    template_name = 'awards.html'
