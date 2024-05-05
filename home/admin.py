from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)

class AnsAdmin(admin.StackedInline):
    model = Ans

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnsAdmin]


admin.site.register(Question)
admin.site.register(Ans)