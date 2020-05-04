
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.listing,name="listing"),
    path('',views.listings,name="listings"),

]
