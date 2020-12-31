from django.contrib import admin
from .models import Fcuser
# Register your models here.


#admin에 출력할 방식
class FcuserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password')


admin.site.register(Fcuser, FcuserAdmin)