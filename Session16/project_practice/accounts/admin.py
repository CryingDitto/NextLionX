# from django.contrib import admin
# from .models import Profile
# # Register your models here.
# admin.site.register(Profile)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile
from .views import CreateUserForm
# Register your models here.


class UserAdmin(BaseUserAdmin):
    add_form = CreateUserForm


admin.site.register(Profile)
