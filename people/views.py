from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from .models import Person

class PersonCreateView(CreateView):
    model = Person
    # template_name = 'people/person_form.html' # и с ним и без него - не работает
    # template_name = 'people/person_form2.html' # и с ним и без него - не работает
    template_name = 'person_form.html' # в корне, т.е. templates/person_form.html - работает
    fields = ('name', 'email', 'job_title', 'bio')

def vacancies(request, ):  # Все вакансии списком   /vacancies

    return render(request, "person/person_form.html", context={ # работает!

    })
