from django.urls import path
from . import views


urlpatterns = {

    path('', views.base, name='base'),
    path('about.html', views.about, name='about'),
    path('services.html', views.services, name='services'),
    path('contact.html', views.contact, name='contact'),
    path('login.html', views.login, name='login'),
    path('reg.html', views.reg, name='sign up'),
    path('appointment.html', views.appointment, name='appointment'),
    path('profile.html', views.profile, name='profile'),
    path('edit.html', views.edit, name='edit'),
    path('settings.html', views.settings, name='settings'),
    path('logout.html', views.logout, name='logout'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('catalog.html', views.catalog, name='catalog'),
    path('learn.html', views.learn, name='learn'),
    path('pharmacy.html', views.pharmacy, name='pharmacy'),




}
