from django.shortcuts import render, get_object_or_404
from .models import User
from django.views import generic



class UserProfileView(generic.View):
    template_name =  "author.html"
    model = User
    def get(self, request, pk, *args, **kwargs):
        context = {
            "profile": get_object_or_404(self.model, id=pk)
            }
        return render(request,self.template_name, context)

userprofile = UserProfileView.as_view()


def usermeprofile(request):
    return render(request, "author.html")
