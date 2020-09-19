from . import views    
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register(r'',views.ProductViewSet )
urlpatterns = [
    path('',include(router.urls))
    ]