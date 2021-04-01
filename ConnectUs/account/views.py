from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from .forms import *


# register new user in database
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect('account:home_page')
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exist(request)
            if destination:
                return redirect(destination)
            return redirect("account:home_page")
        else:
            context['registration_form'] = form

    return render(request, 'account/register.html', context)


def login_view(request, *args, **keargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("account:home_page")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exist(request)
                if destination:
                    return redirect(destination)
                return redirect("account:home_page")
        else:
            context['login_form'] = form
    return render(request, "account/login.html", context)


def get_redirect_if_exist(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def logout_view(request):
    logout(request)
    return redirect("account:home_page")


@login_required(login_url='account:login')
def home_view(request):
    return render(request, 'account/home.html')


@login_required(login_url='account:login')
def profile_view(request, *args, **kwargs):
    context = {}
    user = request.user
    user_id = kwargs.get("user_id")
    if user.is_authenticated:
        try:
            account = Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return HttpResponse("That user doesn't exist.")
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['last_seen'] = account.last_login

        is_self = True
        is_friend = False
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = settings.BASE_URL

    return render(request, 'account/profile.html', context)


@login_required(login_url='account:login')
def search_view_result(request, *args, **kwargs):
    context = {}

    if request.method == "GET":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            search_result = Account.objects.filter(email__icontains=search_query).filter(
                username__icontains=search_query).distinct()
            user = request.user
            accounts = []
            for account in search_result:
                accounts.append((account, False))
            context['accounts'] = accounts

    return render(request, 'account/search_result.html', context)


@login_required(login_url='account:login')
def edit_account_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")

    user_id = kwargs.get("user_id")
    try:
        account = Account.objects.get(pk=user_id)
    except Account.DoesNotExist:
        return HttpResponse("something is wrong")
    if account.pk != request.user.pk:
        return HttpResponse("you can't edit someone elses profile!!!")
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("account:profile_page", user_id=account.pk)
        else:
            form = AccountUpdateForm(request.POST, instance=request.user,
                                     initial={
                                         "id": account.pk,
                                         "email": account.email,
                                         "username": account.username
                                     }
                                     )
            context['form'] = form
    else:
        form = AccountUpdateForm(
            initial={
                "id": account.pk,
                "email": account.email,
                "username": account.username
            }
        )
        context['form'] = form
    return render(request, "account/edit_profile.html", context)

