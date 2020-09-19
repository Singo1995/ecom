from . import views    
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register(r'',views.UserViewSet )
urlpatterns = [
    path('login/',views.signin,name ='signin'),
    path('logout/<int:id>/',views.signout,name ='signout'),
    path('',include(router.urls))
    ]