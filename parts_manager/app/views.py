from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'home/home.html'
