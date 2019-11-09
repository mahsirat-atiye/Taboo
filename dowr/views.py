from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import django.contrib.auth as dj_auth

# Create your views here.
# user views
from analysis import settings
from dowr.models import SignupForm, LoginForm, Category
from django.contrib.auth.models import User


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    elif request.method == "POST":
        f = SignupForm(request.POST)
        if f.is_valid():
            user = f.save()
            # username = f.cleaned_data.get('username')
            # password = f.cleaned_data.get('password')
            # user = dj_auth.authenticate(username=username, password=password)
            dj_auth.login(request, user)
            return HttpResponseRedirect(settings.REDIRECT_URL)

    else:
        f = SignupForm()
    return render(request, 'registration/signup.html', {'form': f})


def game(request):
    if request.method == "POST":
        name11 = request.POST["name11"]
        name12 = request.POST["name12"]
        name21 = request.POST["name21"]
        name22 = request.POST["name22"]
        time = request.POST["time"]
        count = request.POST["count"]
        hardness = request.POST["hardness"]
        category = get_object_or_404(Category, pk=request.POST["choice"])

        if name11 and name12 and name21 and name22:
            context = {
                "name11": name11,
                "name12": name12,
                "name21": name21,
                "name22": name22,
                "time": time,
                "category": category,

            }
            return render(request, 'dowr/game.html', context=context)
        return HttpResponseRedirect(settings.REDIRECT_URL)


def login_(request):
    if request.user.is_authenticated:
        dj_auth.logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
        # return HttpResponse("cici")
    elif request.method == "POST":
        f = LoginForm(data=request.POST)
        if f.is_valid():
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password')
            user = dj_auth.authenticate(username=username, password=password)
            if user is not None:
                dj_auth.login(request, user)
                return HttpResponseRedirect(settings.REDIRECT_URL)
                # return HttpResponse("hihi")
    else:
        f = LoginForm()
    return render(request, 'registration/login.html', {'form': f})
    # return HttpResponse("bibi")


# ======================

def logout_(request):
    return render(request, 'dowr/not_yet_a_user_homepage.html')


def index(request):
    return HttpResponse("hello")


def homepage(request):
    if not request.user.is_authenticated:
        return render(request, 'dowr/not_yet_a_user_homepage.html')

    categories = Category.objects.all()
    return render(request, 'dowr/user_homepage.html', {
        'categories': categories,
    })
