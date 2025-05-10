from contextlib import nullcontext

from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MinLengthValidator
from datetime import datetime

# Определяем варианты для раскрывающегося списка
MENU_CHOICES = [
    ('products', 'Продукты'),
    ('info', 'Информация'),
    ('contacts', 'Контакты'),
]
# выбор строения страхования
build_CHOICES = [
    ('flat', 'Квартира'),
    ('residence', 'Жилой дом'),
    ('apartment', 'Апартаменты'),
]
# объекта страхования - выпадающий список
object_CHOICES = [
    ('Structural_elements', 'Конструктивные элементы'),
    ('interior_decoration', 'Внутренняя отделка и инженерное оборудование'),
    ('household_property', 'Домашнее имущество'),
]
# статус заявки
STATUS_CHOICES = [
    (1, 'Ожидает'),
    (2, 'Обработана'),
    (3, 'Застрахован'),
    (4, 'Отказ'),
]
# Поле с раскрывающимся списком
product_CHOICES = [  # продукт - страница с выбранным продуктом
    ('osago', 'ОСАГО'),
    ('ns', 'Несчастный случай'),
    ('klezh', 'Клещ'),
    ('mortgage', 'Ипотека'),
    ('KASKO', 'КАСКО'),
    ('IFL', 'Имущество физических лиц')
]


# Продукты
class Products(models.Model):
    product = models.CharField(
        max_length=50,
        choices=product_CHOICES,
        default='osago',  # Значение по умолчанию
        verbose_name='Продукты'
    )

    class Meta:
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product


# Инфо о пользователе
class UserInfo(models.Model):
    date_create = models.DateTimeField(auto_now_add=False, default=datetime.now,
                                       verbose_name='Дата создания заявки')  # Дата создания заявки
    fio = models.CharField(max_length=40, verbose_name='ФИО', help_text='Введите свое имя')  # ФИО
    birth_date = models.DateField(default="1900-01-01", verbose_name="Дата рождения")  # Дата рождения
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(7), MaxLengthValidator(11)],
                             verbose_name='Телефон', default='')  # телефон
    email = models.EmailField(max_length=254, default='', unique=False)  # почта
    inn = models.CharField(max_length=12, verbose_name='ИНН (для ЮЛ)', blank=True)  # инн для ЮЛ
    comment = models.CharField(max_length=300, verbose_name='Комментарий', blank=True)  # комментарий

    class Meta:
        abstract = True


class OSAGO(UserInfo):
    mark = models.CharField(max_length=40, verbose_name='Марка авто')  # марка авто
    model = models.CharField(max_length=40, verbose_name='Модель авто')  # модель авто
    year = models.DateField(null=True, default="1900-01-01", validators=[MinValueValidator(1900)],
                            verbose_name='Год выпуска/постройки')  # год выпуска/постройки

    class Meta:
        verbose_name_plural = 'ОСАГО'

    def __str__(self):
        return self.fio


class KASKO(UserInfo):
    mark = models.CharField(max_length=40, verbose_name='Марка авто')  # марка авто
    model = models.CharField(max_length=40, verbose_name='Модель авто')  # модель авто
    year = models.DateField(null=True, default="1900-01-01", validators=[MinValueValidator(1900)],
                            verbose_name='Год выпуска/постройки')  # год выпуска/постройки
    bank = models.CharField(max_length=40, verbose_name='Кредитующий банк', )  # банк
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Стоимость')  # стоимость (страховая сумма)

    class Meta:
        verbose_name_plural = 'КАСКО'

    def __str__(self):
        return self.fio


class NS(UserInfo):
    class Meta:
        verbose_name_plural = "Несчастный случай"

    def __str__(self):
        return self.fio


class Klezh(UserInfo):
    class Meta:
        verbose_name_plural = 'Клещ'

    def __str__(self):
        return self.fio


class IFL(UserInfo):
    class Meta:
        verbose_name_plural = 'Имущество физ лиц'

    def __str__(self):
        return self.fio


class Mortgage(UserInfo):  # Ипотека
    bank = models.CharField(max_length=40, verbose_name='Кредитующий банк', )  # банк
    type_build = models.CharField(
        max_length=20,
        choices=build_CHOICES,
        default='flat',  # Значение по умолчанию
        verbose_name='Строение'
    )
    year = models.DateField(null=True, default="1900-01-01", validators=[MinValueValidator(1900)],
                            verbose_name='Год выпуска/постройки')  # год выпуска/постройки
    risk = models.CharField(
        max_length=50,
        choices=object_CHOICES,
        default='Structural_elements',  # Значение по умолчанию
        verbose_name='Объекта страхования'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Стоимость')  # стоимость (страховая сумма)

    class Meta:
        verbose_name_plural = 'Ипотека'

    def __str__(self):
        return self.fio

    # статус заявки


class OrderStatus(models.Model):
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name_plural = 'Статус заявки'


    def __str__(self):
        return dict(STATUS_CHOICES)[self.status]

# manage.py shell_plus --print-sql
# from movie_app.models import Movie # вход в ORM подключение базы
# from django.db.models import Q # импорт Q
