from django.urls import path
from .views import *

urlpatterns = [

    path('home', home, name='library'),
    path('readers', readers),
    path('save',save_student),

]