from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner,Questions,Choices,Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


#Create class choice inline class with Questions Inlne
class ChoicesInline(admin.StackedInline):
    model = Choices
    extra = 5
    class QuestionsInline(admin.StackedInline):
        model = Questions
        extra = 2

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline]
    list_display = ['content']
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choices)
admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Submission)
