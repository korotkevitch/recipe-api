from django.contrib import admin
from formula.models import Recipe, Ingredient, Tag


admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
