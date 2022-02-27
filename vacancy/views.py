from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        context = {'vacancies': vacancies}
        return render(request, 'vacancy/vacancy.html', context=context)


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')
        user = request.user
        if not user.is_staff:
            return HttpResponseForbidden()
        Vacancy.objects.create(description=description, author=user)
        return redirect('/home')
