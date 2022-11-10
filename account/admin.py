
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm




@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    form_class = UserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', )}),
            (_('user_info'), {'fields': ("bio", 'phone_no', 'profile_pic')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ["username", 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )



