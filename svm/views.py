from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.http import HttpResponse

from forms import ApplicationForm
# Create your views here.


class QuestionnaireView(TemplateView):
    form_class = ApplicationForm
    template_name = 'questionnaire.html'

    def get(self, request):
        form = self.form_class(auto_id=False)
        print 'HOOYYY!!!!'
        return render(request, self.template_name, {'form': form})

class IndexView(TemplateView):

    template_name = 'index.html'


