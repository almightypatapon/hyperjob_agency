from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from resume.models import Resume



class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/main.html')


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        context = {'resumes': resumes}
        return render(request, 'resume/resume.html', context=context)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = AuthenticationForm
    template_name = 'resume/login.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        context = {'user': user}
        return render(request, 'resume/home.html', context=context)


class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')
        user = request.user
        if user.is_staff:
            return HttpResponseForbidden()
        Resume.objects.create(description=description, author=user)
        return redirect('/home')

