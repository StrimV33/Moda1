Сайт разработас при помощи Django, Bootstrap, на платформе Python в приложении PyCharm

Создаем новый проект, в териминале прописываем pip install django, после установки вводим: django-admin startproject name(название нашего проекта, в моем случае "moda".
Проверяем, открываем в терминале файл manage.py, прописываем коману py manage.py ruserver(могут быть иные команды в зависимости от ОС, например(python3 manage.py runserver).
В случае если все правильно, в терминале появляется ссылка на сайт.

Создаем новое приложение командой в терминале py manage.py startapp main(main - название), регестрируем наше приложение в файле settings.py в графе: INSTALLED_APPS, 
добавляем запись с название приложения, у меня 'main'.

Создаем новый файл в приложении с названием urls.py, заходим в главный urls файл ,для того что бы прописать путь к нашему новому urls файлу в приложении:

from django.contrib import admin
from django.urls import path, include - добавляем импорт данных (incude)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  - прописываем такую ссылку на наш новый urls

Создем новую директорию в приложении, называем обязательно templates, в ней создаем еще одну директорию с названием приложения(main), затем создадим html файл, главной страницы.
Создаем метод в файле views для открытия html шаблона:

from django.shortcuts import render

def index(request):
   return render(request, 'main/index.html', data) - (index - название html шаблона, который находить в папке templates/main)
   
Прописываем путь в urls файле к нашему методу:

from django.urls import path
from . import views                -импортируем нам метод 

urlpatterns = [
    path('', views.index, name='home'),  (путь)
    
]

Полный код:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('top', views.top, name='top'),   (путь ко второй странице,котороя появиться позже)
]

Создаю базовый шаблон html для того ,что бы не повторять код на разных страницах, в директории /teplates/main/ назвал base.
Использую встроенный джинджер шобланизатор, код html шаблона:

{%block name(название блока)%}     используем такю конструкцию для данных,который будут отлицаться
Изменяемые данные на разных страницах
{%endblock%}

{% load static %}   - подключение статических файлов ниже более подробное описание
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"> ссылка Bootstrap стиль 
    <link rel="stylesheet" href="{% static 'main/css/main.css' %}"> подгружаем стиль из статических файлов, позже создадим
</head>
<tile>{% block home %}{% endblock %}</tile>  изменяемый блок
<body>
    <aside>
        <img src="{% static 'main/img/m1.jpg' %}" alt="Лого"> подгружаем лого из паки статик
        <span class="logo">ода</span>
        <h3>Навигация</h3>
        <ul>
            <a href="{% url 'home' %}"><li></i>Главная страница</li></a>   Навигация по сайту по нажатию, наши кнопки
            <a href="{% url 'top' %}"><li>Топ</li></a>
            <a href="{% url 'news_home' %}"><li>Новости</li></a>
            <a href="{% url 'create' %}"><li><button class="btn btn-info"><i class="fas fa-plus-circle"></i>Добавить запись</button></li></a> кнопка по добавлению записей
                                                                                                                                              будет описана ниже
        </ul>
    </aside>
    <main>
        {% block body %}
        {% endblock %}
    </main>

</body>
</html>
<header class="mb-auto">
</header>


Создаем папку static, которая упоминалась выше: в ней создаем еще директорию main, в main еще две img - в которой находиться лого сайта, и css .
Так же создаем css файл , я его назвал main.css, в нем настраиваем наш стиль.

Так же необходимо в настойках указать :
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
Чуть ниже настроек:
STATIC_URL = 'static/'         ****


Импортируем настройки статических данных в основном urls файле

from django.contrib import admin
from django.urls import path, include

from django.conf import settings               импорт
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  добовляем папку static (данный с оофициальной документации джанго)


Вот так выглядит шаблон главной страницы:

{% extends 'main/base.html'%} ипортируем из базового шаблона нашу обертку

{% block title %}{{title}}{% endblock %}
{% block home %}Главная страница{% endblock %}

{% block body %}
    <div class="features">
        <h1>{{title}}</h1>
        <p>Сайт разработан при помощи Django, Botstrap</p>
        <h1>Добро пожаловать</h1>
        <p>Первый сайт ,пробная разработка =)</p>
    </div>
{% endblock %}


Создаем новое приложение.(news)  py manage.py startapp news
Поключаем его в основном файлу urls:

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),        подключение  ****
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

Далее создаем в новом прилежении файл urls

from django.urls import path
from . import views


urlpatterns = [
    path('',views.news_home, name='news_home'), подключение функции ,которая будет открывать html шаблон на страницу новости
    path('create',views.create, name='create'), подключение функции о котороя будет описана ниже
]


Создим таблицу в базе данных,для ввода данных и в дальнейшем ,для отображения на сйате

в файле models.py

from django.db import models


class Articles(models.Model):           Создаем класс 
    title = models.CharField('Название', max_length=50)    для заголовка
    anons = models.CharField('Анонс', max_length=250)     для примечания
    text = models.TextField('Статья')                      для описания
    date = models.DateTimeField('Дата публикации')         для времени ,когда была сделана запись
    image = models.ImageField(verbose_name='Фото',null=True, blank=True, upload_to='news/img/')    для загрузки фото

    def __str__(self):
        return f'Новость:{self.title}'

    class Meta:     так же создаем класс ,для изменения названия таблицы в панели администратора
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        

Регистрируем нашу таблицу в файле admin.py


from django.contrib import admin
from .models import Articles        импортируем из файла models

admin.site.register(Articles)     регистрируем



Далее необходимо провести миграции 
Заходим в терминал файла manage.py
Вводим: py manage.py makemigrations добовляем файлы в миграцию
И затем: py manage.py migrate

После миграций нам нужно создать пользователя для входа в панель администратора
Прописываем команду: py manage.py createsuperuser
Вводим имя пользователя и пароль,(почту не обязательно)


В файле views

from django.shortcuts import render, redirect
from .models import Articles   импортируем из models класс Articles


def news_home(reqest):  прописываем функцию для вывода данных из таблицы на страницу новости
    news = Articles.objects.order_by('-date')         (date - сортировка данных, по дате,так же можно сортировать по другим данным)
    return render(reqest,'news/news_home.html', {'news': news}) 
    

Создаем шаблон news_home

{% extends 'main/base.html'%}   добовляем шаблон из директории main

{% block title %}Новости на сайте{% endblock %}
{% block home %}Новости на сайте{% endblock %}

{% block body %}
    <div class="features">
        <h1>Новости на сайте</h1>
        <p>Сайт разработан при помощи Django, Botstrap</p>
        <h1>Новости моды</h1>
        {% if news %}                                 для более коректного вывода используем цикл for внутри нашего шаблона
            {% for i in news %}                       форма for - {% for i in news %} , выводим i {% i.title %} и закрываем цикл(обязательно) {% endfor %}
                <div class="alert alert-warning">
                    <h3>{{ i.title }}</h3>            выводим название
                    <img src = {{ i.image }}>         фото
                    <p>{{ i.text }} </p>              текст
                </div>
            {% endfor %}
        {% else %}
            <p>У вас нет записей</p>                  конструкция if по такая же как и for 
        {% endif %}
    </div>
{% endblock %}

Так же прописываем стили в нашем css файле для отоброжения новостей.


создаем новый html шаблон create


{% extends 'main/base.html'%}     добовляем шаблон из директории main

{% block title %}Форма по добавлению статьи{% endblock %}
{% block home %}Форма по дабавлению статьи{% endblock %}

{% block body %}
    <div class="features">
        <h1>Форма по добавлению статьи</h1>
        <form method="post">
            {% csrf_token %}       подключаем csrf token для создания форм
            {{ form.title }}<br>   форма для добавления названия
            {{ form.anons }}<br>   форма для добавления примечания
            {{ form.text }}<br>    форма для добавления текста
            {{ form.date }}<br>    форма для добавления даты
            {{ form.image }}<br>   форма для добавления фото
            <span {{ error }}></span>
            <button class="btn btn-success" type="sumbit">Добавить запись</button>  кнопка для добовления записи

        </form>
    </div>
{% endblock %}

Шаблон готов,теперь опишем форму
Создаем файл forms.py

from .models import Articles                                                                   импортируем модель Articles  
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput              импортируем различные формы для отдельных данных



class ArticlesForm(ModelForm):          создаем класс
    class Meta:
        model = Articles
        fields = ['title','anons','text','date','image']  вписываем в список поля для ввода,которые у нас в файле models класс Articles

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'     placegolder выводит текст в форме для удобства заполнения пользователю
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата добавления'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'image': FileInput(attrs={
                'class': 'form-control',
                'placehilder': 'Фото статьи'
            })
        }


from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_home(reqest):
    news = Articles.objects.order_by('-date')
    return render(reqest,'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не верная, проверьте данные'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)


Так же создадим функцию для проверки данных в файле views.py


from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm   импортируем нашу форму 


def news_home(reqest):
    news = Articles.objects.order_by('-date')
    return render(reqest,'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':           проверяем ,то что данные идут из формы
        form = ArticlesForm(request.POST)  сохраняет данные от пользователя из формы
        if form.is_valid():                
            form.save()                    если данные коректны ,то они сохраняются
            return redirect('news_home')
        else:
            error = 'Форма не верная, проверьте данные'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)
