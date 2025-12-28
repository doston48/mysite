from django.contrib import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('about/',views.about),
] 