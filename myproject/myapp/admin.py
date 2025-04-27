from django.contrib import admin
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin 

from .models import Drinks
from .models import Menu
from .models import MenuCategory
from .models import Booking
from .models import Person
admin.site.register(Drinks)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Booking)
admin.site.unregister(User) 
# Register your models here.
@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ] 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 
# Hủy đăng ký mô hình Person nếu đã được đăng ký
try:
    admin.site.unregister(Person)
except admin.sites.NotRegistered:
    pass  # Nếu chưa đăng ký, không làm gì cả
@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", ) 
    