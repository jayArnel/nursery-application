import json
import cPickle as pickle

from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse

from forms import ApplicationForm
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'


class QuestionnaireView(TemplateView):
    form_class = ApplicationForm
    template_name = 'questionnaire.html'

    def get(self, request):
        form = self.form_class(auto_id=False)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name =(str(form.cleaned_data['name'])) 
            X = []
            X.append(str(form.cleaned_data['parents']))
            X.append(str(form.cleaned_data['has_nurs']))
            X.append(str(form.cleaned_data['form']))
            X.append(str(form.cleaned_data['children']))
            X.append(str(form.cleaned_data['housing']))
            X.append(str(form.cleaned_data['finance']))
            X.append(str(form.cleaned_data['social']))
            X.append(str(form.cleaned_data['health']))
            encoders = pickle.load(open('svm/pickles/encoders.pickle', 'r'))
            for i in range(0, len(X)):
                X[i] = encoders[i].transform([str(X[i])])[0]
            svm = pickle.load(open('svm/pickles/svm.pickle', 'r'))
            print X
            prediction = svm.predict(X)
            label = encoders[-1].inverse_transform(prediction)
            if label[0] == 'not_recom':
                label = 'Not Recommended'
            elif label[0] == 'spec_prior':
                label = 'Special Priority'
            elif label[0] == 'priority':
                label = 'Priority'
            elif label[0] == 'recommended':
                label = 'Recommended'
            if label[0] == 'very_recom':
                label = 'Very Recommended'                

            return HttpResponse(
                json.dumps({'name':name,"prediction": label}),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps(form.errors),
                content_type="application/json"
            )
