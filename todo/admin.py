from django.contrib import admin
from .models import todo_model


# Register your models here.
class todo_model_Admin(admin.ModelAdmin):
    readonly_fields = ('Created_time',)


admin.site.register(todo_model, todo_model_Admin)
