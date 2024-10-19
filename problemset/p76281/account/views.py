from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import SignUpForm, LoginForm, TeamForm
from account.models import Account, Team


def home(request):
    try:
        team = request.user.account.team.name
    except:
        team = None
    return render(request, 'home.html', context={'team': team})


def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('team')
        else:
            return render(request, 'signup.html', {'form': form})


def login_account(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = Account.objects.get(username=form.cleaned_data['username'])
                if user.check_password(form.cleaned_data['password']):
                    login(request, user)
                    return redirect('home')
            except Account.DoesNotExist:
                return render(request, 'login.html', {'form': form})
        return render(request, 'login.html', {'form': form})



def logout_account(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')



@login_required
def joinoradd_team(request):
    if request.method == 'GET':
        if request.user.account.team:
            return redirect('home')
        else:
            form = TeamForm()
            return render(request, 'team.html', context={'form': form})
    elif request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            try:
                team = Team.objects.get(name=form.cleaned_data['name'])
            except Team.DoesNotExist:
                team = Team.objects.create(
                    name=form.cleaned_data['name'],
                    jitsi_url_path=f'http://meet.jit.si/{form.cleaned_data['name']}'
                )
            request.user.account.team = team
            request.user.account.save()
        return redirect('home')




def exit_team(request):
    if request.method == 'GET':
        request.user.account.team = None
        request.user.account.save()
        return redirect('home')
