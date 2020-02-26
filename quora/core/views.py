from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from questans.models import Question, Answer
from .forms import RegisterForm, LoginForm
from .models import User


class DashboardView(FormView):

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            ques_obj = Question.objects.filter(user=user)
            ans_obj = None
            if ques_obj:
                ans_obj = Answer.objects.filter(question=ques_obj[0])
            content['userdetail'] = user
            content['questions'] = ques_obj
            content['answers'] = ans_obj
            return render(request, 'dashboard.html', content)
        return redirect(reverse('login-view'))

class RegisterView(FormView):

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)

class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + str(e)
            return render(request, 'login.html', content)

class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')