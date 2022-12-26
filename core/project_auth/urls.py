from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
app_name = 'my_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('create_user', views.CustomUserCreateView.as_view(), name='create_user')
]
