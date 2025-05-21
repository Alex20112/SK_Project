from tempfile import template

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from PSB_app.views import menu, total_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('', menu),
    path('all/', total_list),

]
