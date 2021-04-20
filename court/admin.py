from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(CaseType)

admin.site.register(Year)
admin.site.register(InternelCategory)
admin.site.register(Department)
admin.site.register(Commissions)
admin.site.register(ConstituionalBodies)
admin.site.register(BoardsandCorporations)
admin.site.register(userinfo)
admin.site.register(othersdoc)

# @admin.register(formDetails)
# class formDetailsAdmin(admin.ModelAdmin):
#     list_display = ("Casetypes", "years")