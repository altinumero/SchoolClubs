from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'clubs/home.html')


def all_clubs(request):
    return render(request, 'clubs/allClubs.html')


def announcement(request):
    return render(request, 'clubs/announcements.html')


def post(request):
    return render(request, 'clubs/posts.html')


def messages(request):
    return render(request, 'clubs/message.html')


def clupDetail(request):
    return render(request, 'clubs/detailPage.html')
