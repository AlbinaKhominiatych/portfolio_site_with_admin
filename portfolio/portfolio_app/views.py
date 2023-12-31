from django.views.generic import TemplateView, ListView
from portfolio_app.models import Project

from django.views.generic import DetailView
from .models import Name, Profession, Description, Experience, Photo

from django.shortcuts import render

class IndexView(TemplateView):
        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            name = Name.objects.first()
            experience = Experience.objects.first()
            context['first_name'] = name.first_name
            context['last_name'] = name.last_name
            context['profession'] = Profession.objects.first()
            context['description'] = Description.objects.first()
            context['start_year'] = experience.start_year
            context['end_year'] = experience.end_year
            context['position'] = experience.position
            context['description_experience'] = experience.description_experience
            # Додаємо нову змінну, яка міститиме результат обчислення тривалості досвіду
            context['experience_duration'] = experience.end_year - experience.start_year
            context['photo'] = Photo.objects.first()
            return context

class ProjectListView(ListView):
        model = Project
        template_name = 'project_list.html'
        context_object_name = 'projects'

def post(self, request, *args, **kwargs):
            form = Photo(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return super().get(request, *args, **kwargs)

def index(request):
    context = {
        'photo': Photo.objects.first(),
    }
    return render(request, 'index.html', context)