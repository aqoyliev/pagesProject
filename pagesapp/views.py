from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SettingsPageView(TemplateView):
    template_name = 'settings.html'

class SignupPageView(TemplateView):
    template_name = 'signup.html'