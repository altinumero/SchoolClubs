from django.contrib import admin

from clubs.models import *


class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Student, StudentAdmin)


class AdvisorAdmin(admin.ModelAdmin):
    class Meta:
        model = Advisor
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Advisor, AdvisorAdmin)


class AdministrationAdmin(admin.ModelAdmin):
    class Meta:
        model = Administration
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Administration, AdministrationAdmin)


class ClubAdmin(admin.ModelAdmin):
    class Meta:
        model = Club
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Club, ClubAdmin)


class ClubStudentAdmin(admin.ModelAdmin):
    class Meta:
        model = ClubStudent
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(ClubStudent, ClubStudentAdmin)


class AnnouncementAdmin(admin.ModelAdmin):
    class Meta:
        model = Announcement
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Announcement, AnnouncementAdmin)


class SurveyAdmin(admin.ModelAdmin):
    class Meta:
        model = Survey
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Survey, SurveyAdmin)


class DiscussionAdmin(admin.ModelAdmin):
    class Meta:
        model = Discussion
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Discussion, DiscussionAdmin)


class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Comment, CommentAdmin)


class PostsAdmin(admin.ModelAdmin):
    class Meta:
        model = Posts
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(Posts, PostsAdmin)


class MessageDialogAdmin(admin.ModelAdmin):
    class Meta:
        model = MessageDialog
        list_display = '__all__'
        list_display_links = '__all__'
        search_fields = '__all__'
        list_filter = '__all__'


admin.site.register(MessageDialog, MessageDialogAdmin)