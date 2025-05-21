from django.shortcuts import render
from PSB_app.models import Products, STATUS_CHOICES, MENU_CHOICES, Klezh


def menu(request):
    start_list_menu = MENU_CHOICES
    return render(request, 'start_list_menu.html', {'start_list_menu':start_list_menu})


def total_list(request):
    all = Klezh.objects.all().values()
    return render(request, 'total_list.html', {'all':all})