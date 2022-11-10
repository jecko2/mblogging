from django.urls import path
from creation import views as create_view

urlpatterns = [
    
    path("tags/create/", create_view.CreateTag.as_view(), name="tag_create"),
    path("posts/create/", create_view.CreatePost.as_view(), name="post_create"),

]
