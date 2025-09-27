from django.urls import path

from . import views
from .views import PortfolioView, UserLoginView, UserLogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PortfolioView

app_name = 'pages'

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('download-resume/', views.download_resume, name='download_resume'),
    path('contact-submit/', views.contact_submit, name='contact_submit')
]