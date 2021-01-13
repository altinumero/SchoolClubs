from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'clubs/home.html')


def all_clubs(request):
    return render(request, 'clubs/allClubs.html')


def announcement(request):
    return render(request, 'clubs/announcements.html')


def post(request):
    return render(request, 'clubs/posts.html')


def chat(request):
    return render(request, 'clubs/chat.html')


def survey(request):
    return render(request, 'clubs/surveys.html')


def discussion(request):
    return render(request, 'clubs/discussions.html')


def messages(request):
    return render(request, 'clubs/message.html')


def clupDetail(request):
    return render(request, 'clubs/detailPage.html')


def userPage(request):
    return render(request, 'clubs/userpage.html')


def addEvent(request):
    return render(request, 'forms/addEvent.html')


def addPost(request):
    return render(request, 'forms/addPost.html')


def addSurvey(request):
    return render(request, 'forms/addSurvey.html')


def addDiscussion(request):
    return render(request, 'forms/addDiscussion.html')


def join(request):
    return render(request, 'forms/join.html')


def report(request):
    return render(request, 'forms/report.html')
