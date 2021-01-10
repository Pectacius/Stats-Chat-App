from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from friendship.models import Friend
from friendship.models import FriendshipRequest


def index(request) -> HttpResponse:
    return render(request, 'chat/index.html')


def room(request, room_name) -> HttpResponse:
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user': request.user.username,
    })


@login_required
def add_friend(request, user_id) -> HttpResponse:
    other_user = User.objects.get(pk=user_id)
    Friend.objects.add_friend(request.user, other_user, message="Hi! I would like to add you uwu")
    return HttpResponse("Friend request sent")


@login_required
def accept_friend_request(request, user_id) -> HttpResponse:
    friend_request = FriendshipRequest.objects.get(to_user=request.user.id, from_user=user_id)
    friend_request.accept()
    return HttpResponse("Friend request accepted")


@login_required
def decline_friend_request(request, user_id) -> HttpResponse:
    friend_request = FriendshipRequest.objects.get(to_user=request.user.id, from_user=user_id)
    friend_request.reject()
    return HttpResponse("Friend request rejected")


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('index'))
        else:
            print(form.errors)
    return render(request, 'chat/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('log_in'))
        else:
            print(form.errors)
    return render(request, 'chat/signup.html', {'form': form})