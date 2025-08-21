from django.contrib import admin
from . models import Post, Category, Profile, Comment, AffiliateLink, Services

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Services)
admin.site.register(AffiliateLink)