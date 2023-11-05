from django.contrib import admin
from blog.models import Post
# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Site"

blog_admin = BlogAdminArea(name="Blog Admin")

blog_admin.register(Post)