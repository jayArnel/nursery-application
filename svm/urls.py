from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^questionnaire/$', views.QuestionnaireView.as_view(), name='questionnaire')
]
