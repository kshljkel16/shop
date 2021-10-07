from django.urls import path
from account.views import *

urlpatterns = [
    path('register/',ReqistrationView.as_view()),
    path('activate/',ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/',LogoutView.as_view()),

]