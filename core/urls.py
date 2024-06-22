from django.urls import path
from .views import homepage, aboutpage
from . import views


urlpatterns = [
    path("", homepage, name="homepage"),
    path("about", aboutpage, name="aboutpage"),
    

]
