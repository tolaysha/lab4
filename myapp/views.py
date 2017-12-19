from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


# Create your views here.

def notif(request):
    form = Subscruberforms(request.POST or None)
    if request.POST and form.is_valid():
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()
    return render(request, 'notif.html', locals())


def main(request):
    return render(request, 'main.html')


def test(request):
    return render(request, 'test.html')


def h3(request):
    return render(request, 'h3.html')


def about(request):
    return render(request, 'about.html')


class subs_view(ListView):
    model = Subscribers
    template_name = "test.html"


class reg(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "reg.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(reg, self).form_valid(form)



class auth1(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "auth.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(auth1, self).form_valid(form)




