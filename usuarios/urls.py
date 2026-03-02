from django.urls import path
from django.contrib.auth import views as auth_views
from .views import lista_perfiles, dashboard, registro, logout_view


urlpatterns = [
    path('', lista_perfiles, name='lista_perfiles'),
    path('dashboard/', dashboard, name='dashboard'),
    path('registro/', registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    
]
