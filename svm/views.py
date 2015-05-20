from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from forms import ApplicationForm
# Create your views here.

class IndexView(TemplateView):
    form_class = ApplicationForm
    template_name = 'index.html'

    def get(self, request):
        form = self.form_class(auto_id=False)
        print dir(form)
        return render(request, self.template_name, {'form': form})