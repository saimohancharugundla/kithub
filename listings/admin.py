from django.contrib import admin
from .models import Listing
# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('id','title','owner','category','sub_category','price','is_published','list_date')
    list_display_links = ('id','title')
    list_filter = ('category','sub_category')
    search_fields = ('title','description','price')
    list_per_page = 30

admin.site.register(Listing,ListAdmin)