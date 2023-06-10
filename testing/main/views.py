from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib.auth.forms import  AuthenticationForm
from itertools import chain
from .forms import *
from .models import *

# Главная страницв
def index(request):
    table = Table.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная', 'table': table})

# О Нас
def about_us(request):
    return render(request, 'main/about.html')

# Контакты
def contacts(request):
    return render(request, 'main/contacts.html')

# Услуги
def doing(request):
    return render(request, 'main/doing.html')

#Регистрация
class RegisterFormView(FormView):
    form_class = RegisterUserForms

    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

# Авторизация
class LoginUser(LoginView):
    form_class = AuthenticationForm

    template_name = 'main/login.html'

    def form_valid(self, form):
        return super(LoginUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginUser, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')

# Выход пользователя
def LogoutUser(request):
    logout(request),
    return redirect('login')

# Мои заявки
def MyTask(request):
    table = sorted(chain(Form.objects.filter(nikname=request.user), Form2.objects.filter(nikname=request.user),
                         Form3.objects.filter(nikname=request.user), Form4.objects.filter(nikname=request.user),
                         Form5.objects.filter(nikname=request.user), Form6.objects.filter(nikname=request.user), ),
                   key=lambda instance: instance.status)
    q = request.GET.get('q')
    if q:
        if q.lower() == 'регистрация прав':
            table = Form.objects.all()
        elif q.lower() == 'кадастровый учёт':
                table = Form2.objects.all()
        elif q.lower() == 'единая процедура':
                table = Form3.objects.all()
        elif q.lower() == 'получить консультацию':
                table = Form5.objects.all()
        elif q.lower() == 'выездное обслуживание':
                table = Form6.objects.all()
        elif q.lower() == 'оформить недвижемость':
                table = Form4.objects.all()
        elif q=='':
            table = sorted(chain(Form.objects.filter(nikname=request.user), Form2.objects.filter(nikname=request.user),
                                 Form3.objects.filter(nikname=request.user), Form4.objects.filter(nikname=request.user),
                                 Form5.objects.filter(nikname=request.user),
                                 Form6.objects.filter(nikname=request.user), ),
                           key=lambda instance: instance.status)
        else:
            table = []

    else:
        table = sorted(chain(Form.objects.filter(nikname=request.user), Form2.objects.filter(nikname=request.user),
                             Form3.objects.filter(nikname=request.user), Form4.objects.filter(nikname=request.user),
                             Form5.objects.filter(nikname=request.user), Form6.objects.filter(nikname=request.user), ),
                       key=lambda instance: instance.status)
    return render(request, 'main/mytask.html', {'table': table})

# Регистрация прав
def register_right(request):
    error = ''
    form = FormForm({
        'nikname': request.user,
        'razdel': 'Регистрация прав',
        'status': '1'

    })
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/register_right.html', context)

# Кадастровй учёт
def form2_v(request):
    error = ''
    form = Form2Form({
        'nikname': request.user,
        'razdel': 'Кадастровый учёт',
        'status': '1'

    })
    if request.method == 'POST':
        form = Form2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/form2.html', context)

# Единая процедура
def form3_v(request):
    error = ''
    form = Form3Form({
        'nikname': request.user,
        'razdel': 'Единая процедура',
        'status': '1'

    })
    if request.method == 'POST':
        form = Form3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/form3.html', context)

# оформить недвижемость
def form4_v(request):
    error = ''
    form = Form4Form({
        'nikname': request.user,
        'razdel': 'Оформление недвижемости',
        'status': '1'

    })
    if request.method == 'POST':
        form = Form4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/form4.html', context)

# Получить консультацию
def form5_v(request):
    error = ''
    form = Form5Form({
        'nikname': request.user,
        'razdel': 'Получить консультацию',
        'status': '1'

    })
    if request.method == 'POST':
        form = Form5Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/form5.html', context)

# Выездное обслуживание
def form6_v(request):
    error = ''
    form = Form6Form({
        'nikname': request.user,
        'razdel': 'Выездное обслуживание',
        'status': '1'

    })
    if request.method == 'POST':
        form = Form6Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/form6.html', context)


# Добавление в Регистрация прав
def Update(request, pk):
    template = 'main/register_right.html'
    get_article = Form.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('mytask')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': FormForm(instance=get_article)
    }

    return render(request, template, context)


def Update2(request, pk):
    template = 'main/form2.html'
    get_article = Form2.objects.get(pk=pk)
    if request.method == 'POST':
        form = Form2Form(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('mytask')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': Form2Form(instance=get_article)
    }

    return render(request, template, context)


def Update3(request, pk):
    template = 'main/form3.html'
    get_article = Form3.objects.get(pk=pk)
    if request.method == 'POST':
        form = Form3Form(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('mytask')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': Form3Form(instance=get_article)
    }

    return render(request, template, context)


def Update4(request, pk):
    template = 'main/form4.html'
    get_article = Form4.objects.get(pk=pk)
    if request.method == 'POST':
        form = Form4Form(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('mytask')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': Form4Form(instance=get_article)
    }

    return render(request, template, context)


def Update5(request, pk):
    template = 'main/form5.html'
    get_article = Form5.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('mytask')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': Form5Form(instance=get_article)
    }

    return render(request, template, context)


def Update6(request, pk):
    template = 'main/form6.html'
    get_article = Form6.objects.get(pk=pk)
    if request.method == 'POST':
        form = Form6Form(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('mytask')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': Form6Form(instance=get_article)
    }

    return render(request, template, context)

# Удаление Регистрации прав остальные как и формы
def DELIT1(request, pk):
    get_article = Form.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('mytask'))


def DELIT2(request, pk):
    get_article = Form2.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('mytask'))


def DELIT3(request, pk):
    get_article = Form3.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('mytask'))


def DELIT4(request, pk):
    get_article = Form4.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('mytask'))


def DELIT5(request, pk):
    get_article = Form5.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('mytask'))


def DELIT6(request, pk):
    get_article = Form6.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('mytask'))

