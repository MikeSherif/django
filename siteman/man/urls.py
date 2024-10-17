from django.urls import path, re_path, register_converter
from man import views, converters

register_converter(converters.FourDigitYearConverter, "year4"),

urlpatterns = [
    path('', views.index, name='main'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]
