from django.contrib import admin
from .models import Post

# Third Parties Libraries
# from image_cropping import ImageCroppingMixin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('author', 'created', 'status', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hiearchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)

# Costume Model Admin by Django-Taggit
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super(MyModelAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())