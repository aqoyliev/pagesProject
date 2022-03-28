from django.urls import path
from .views import HomePageView, AboutPageView, SettingsPageView, SignupPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('settings/',SettingsPageView.as_view(),name='settings'),
    path('signup/',SignupPageView.as_view(),name='signup')
]