from django.shortcuts import render
from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name

class IndexTwoTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index2.html"
        return template_name