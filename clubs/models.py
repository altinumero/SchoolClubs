from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    userId = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    department = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.first_name


class Advisor(models.Model):
    userId = models.CharField(max_length=150, unique=True, )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    department = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.first_name


class Administration(models.Model):
    president = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='president', related_query_name='president')
    advisor = models.OneToOneField(Advisor, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='advisor', related_query_name='advisor')
    vicePresident = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='vicePresident', related_query_name='vicePresident')
    agent = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='agent', related_query_name='agent')
    accountant = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='accountant', related_query_name='accountant')
    secretary = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='secretary', related_query_name='secretary')


class Club(models.Model):
    club_name = models.CharField(max_length=150, )
    email = models.EmailField(blank=True)
    advisor = models.OneToOneField(Advisor, on_delete=models.CASCADE, blank=True, null=True)
    club_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    administration = models.OneToOneField(Administration, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name


class ClubStudent(models.Model):
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)


class Announcement(models.Model):
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    publisher = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)


class Survey(models.Model):
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    end_date = models.DateTimeField(auto_now_add=False, null=True, blank=True, )
    question = models.TextField(blank=True, null=True)
    publisher = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    yes = models.BooleanField(blank=True, null=True)
    no = models.BooleanField(blank=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)


class Discussion(models.Model):
    topic = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    publisher = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, models.SET_NULL, blank=True, null=True)
    person = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )


class Posts(models.Model):
    publisher = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    content = models.TextField(blank=True, null=True)


class MessageDialog(models.Model):
    sender = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True,
                               related_name='senders', related_query_name='sender')
    receiver = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True,
                                 related_name='receivers', related_query_name='receiver')
    content = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
