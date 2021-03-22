from django.contrib import admin

from pages.models import Rubric, Post, Image

@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ["name","url"]
    prepopulated_fields = {"url":("name",),}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","rubric","foto_post","url",
                    "post_data","post_update"]
    prepopulated_fields = {"url":("title",),}

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["name","image","url"]
    prepopulated_fields = {"url":("name",),}
