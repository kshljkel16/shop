from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import OrderViewset

router = DefaultRouter()
router.register('orders',OrderViewset)

urlpatterns =[
    path("",include(router.urls))
    ]
