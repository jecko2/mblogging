from django.urls import path
from .views import userprofile, usermeprofile


urlpatterns = [
    path("", usermeprofile, name="about_me"),
    path("<int:pk>/", userprofile, name="account_detail"),
]

