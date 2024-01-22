# Name: Connor Warner
# Class: CIS 218
# Date: 1/24/24

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """ Template for home/resume page"""
    template_name = "home.html"

class ProjectsPageView(TemplateView):
    """ Template for projects page"""
    template_name = "projects.html"

class ContactPageView(TemplateView):
    """ Template for contact page"""
    template_name = "contact.html"