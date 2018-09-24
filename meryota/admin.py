from django.contrib import admin
from .models import *
#from .models import Question, Choice, Article, Category, Person, Group, Membership

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'pub_date')
    search_fields = ['title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

##demo many to many
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)


