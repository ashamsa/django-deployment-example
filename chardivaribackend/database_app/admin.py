from django.contrib import admin

from .models import House
from .models import A_User
from .models import Province
from .models import City

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['listing_type','house_type']
    search_fields = ['city']
    list_filter = ['house_type','listing_type','parking','furnished','create_Date','availability']
    date_hierarchy = 'create_Date'
    ordering = ['-create_Date']


@admin.register(A_User)
class A_User_Admin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    search_fields = ('first_name', 'last_name')
    date_hierarchy = 'create_Date'
    ordering = ['-create_Date']


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['province_name']
    search_fields = ['province_name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

