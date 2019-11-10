from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import django.contrib.auth as dj_auth
import json
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
        dowr_time = request.POST["time"]
        # time of each dowr
        num_of_dowrs = request.POST["count"]
        hardness = request.POST["hardness"]
        category = get_object_or_404(Category, pk=request.POST["choice"])
        list_of_words=category.word_set.filter(hardness_level=hardness)
        team_time_limit = int(dowr_time)*int(num_of_dowrs)*0.7
        list_of_word = []
        for word in list_of_words:
            list_of_word.append(word.name)

        if name11 and name12 and name21 and name22:
            context = {
                "name11": name11,
                "name12": name12,
                "name21": name21,
                "name22": name22,
                "category": category,
                "dowr_time": dowr_time,
                "num_of_dowrs": num_of_dowrs,
                "list_of_word":list_of_word,
                "team_time_limit": team_time_limit

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
