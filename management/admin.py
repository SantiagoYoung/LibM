from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline, )

class BookInline(admin.TabularInline):
    model = Book


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',{'fields': ['name']}),
        ('Price',{'fields': ['price']}),
        ('Author',{'fields': ['author']}),
        ('Category', {'fields': ['category']}),
        ('Date information',{'fields': ['publish_date']}),

    ]
    # inlines = (BookInline,)   ...need ForeignKey
    list_filter = ['name', 'author', 'category']
    list_display = ['name', 'author', 'category']
    search_fields = ['name', 'author', 'categoty']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Img)
admin.site.register(MyUser)
admin.site.register(MySiteProfile)