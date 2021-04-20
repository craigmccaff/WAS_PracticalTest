from django.contrib import admin

from .models import Post

# user = admin
# password = 123456

admin.site.site_header = "News Story Admin"
admin.site.site_title = "News Story Admin Area"
admin.site.index_title = "Welcome to the News Story Admin Area"


class PostAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['post_heading']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                 (None, {'fields': ['post_text']}), ]


admin.site.register(Post, PostAdmin)
