from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_view(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    context = {'students': students}

    return render(request, template, context)
# .prefetch_related('teachers').order_by('group')