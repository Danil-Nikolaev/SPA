from django.contrib import admin
from page.models import SPA

# Register your models here.


@admin.register(SPA)
class SPAAdmin(admin.ModelAdmin):
    pass

