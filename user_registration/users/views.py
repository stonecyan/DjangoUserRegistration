from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser


@login_required
def homeView(request):

    if request.user.is_superuser:
        usersObject = CustomUser.objects.all()
        return render(request, 'admin.html', {'users': usersObject})
    return render(request, 'home.html')


def registerView(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, you are now able to login!')
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


class UserCreateView(UserPassesTestMixin, CreateView):
    form_class = CustomUserForm
    template_name = 'user_form.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser

    # def get_absolute_url(self):
    #     return reverse('user-home')


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'first_name', 'last_name', 'email', 'website']
    template_name = 'user_form.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser
