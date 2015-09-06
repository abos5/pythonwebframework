from django.contrib import admin
from cate.models import Category


@admin.register(Category)
class CateAdmin(admin.ModelAdmin):
    pass


# Register your models here.
