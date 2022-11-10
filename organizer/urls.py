from django.urls import path
from . import views
from search import views as search_views

urlpatterns = [
    path("", views.ViewHome.as_view(), name='home'),
    path("tags/", views.TagHomeView.as_view(), name="tag_list"),
    path("search/", search_views.SearchBlogView.as_view(), name="search"),
   
    path("<int:year>/<int:month>/<int:day>/<str:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    
    path("tag/<str:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
]

