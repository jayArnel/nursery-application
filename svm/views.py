import json
import cPickle as pickle

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
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            X = []
            X.append(str(form.cleaned_data['parents']))
            X.append(str(form.cleaned_data['has_nurs']))
            X.append(str(form.cleaned_data['form']))
            X.append(str(form.cleaned_data['children']))
            X.append(str(form.cleaned_data['housing']))
            X.append(str(form.cleaned_data['finance']))
            X.append(str(form.cleaned_data['social']))
            X.append(str(form.cleaned_data['health']))
            encoders = pickle.load(open('svm/pickles/encoders.pickle','r'))
            for i in range(0, len(X)):
                X[i] = encoders[i].transform([str(X[i])])[0]
            svm = pickle.load(open('svm/pickles/svm.pickle','r'))
            print X
            prediction = svm.predict(X)
            label = encoders[-1].inverse_transform(prediction)
            return HttpResponse(
                json.dumps({"prediction": label[0]}),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps(form.errors),
                content_type="application/json"
            )
