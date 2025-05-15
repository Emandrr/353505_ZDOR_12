from django.contrib import admin
from .models import AutoCompany, News, FAQ, Vacancy, Promo, CustomUser, Car
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'phone', 'birth_date', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'birth_date')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'birth_date', 'password1', 'password2', 'is_staff', 'is_active', 'image', 'additional_info')}
         ),
    )

    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)


    class Meta:
        proxy = True
        app_label = 'auth'


admin.site.register(AutoCompany)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(Vacancy)
admin.site.register(Promo)
admin.site.register(Car)