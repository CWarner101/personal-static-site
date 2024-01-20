from django.urls import path

from .views import HomePageView, ProjectsPageView, ContactPageView

urlpatterns = [
    path("contact/", ContactPageView.as_view(), name='contact'),
    path("projects/", ProjectsPageView.as_view(), name='projects'),
    path("", HomePageView.as_view(), name="home"),
]
