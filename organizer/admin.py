from django.contrib import admin
from .models import Post, Alert, PostImage

def makepostpublic(modelName, request, queryset):
    queryset.update(public=True)
makepostpublic.shortdescription = "Make post public"
def unpublishpost(modelName, request, queryset):
    queryset.update(public=False)
makepostpublic.shortdescription = "Unpublish post"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title", )}
    actions = [makepostpublic, unpublishpost]
    list_display = ['title', 'public', "author", "pub_date", "slug", "tag", "genre"]



@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    pass



@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
