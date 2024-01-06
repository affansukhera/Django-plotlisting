from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from .forms import LogInForm, SIGNUPForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LogInForm
    success_url = '/home/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect("home")
        else:
            messages.error(self.request, "Invalid username or password")
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SIGNUPForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class ChangePasswordView(FormView):
    template_name = 'change-password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)