from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View,TemplateView,FormView,CreateView

from social.forms import RegistrationForm

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

# def post(self,request,*args,**kwargs):
#     form=RegistrationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("sign_up")
#     else:
#         return render(request,"register.html",{"form":form})

    def get_success_url(self):
        return reverse("signup")
    


