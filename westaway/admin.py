from django.contrib import admin

from .models import Opponent, Entry, Image, Competition, PasswordEntry, User

# Register your models here.
admin.site.register(Opponent)
admin.site.register(Entry)
admin.site.register(Competition)
admin.site.register(PasswordEntry)
admin.site.register(User)

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "photo"]

admin.site.register(Image, imageAdmin)
