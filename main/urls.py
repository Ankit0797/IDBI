from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crf', views.CRF, name='CRF'),
    # path('view_all_emp', views.view_all_emp, name='view_all_emp'),
    # path('add_emp', views.add_emp, name='add_emp'),
    # path('remove_emp', views.remove_emp, name='remove_emp'),
    # path('filter_emp', views.filter_emp, name='filter_emp'),
] 