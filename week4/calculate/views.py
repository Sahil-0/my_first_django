from django.shortcuts import render
from django import views

from .forms import MathForm
from calculate import math_operation


class AddTwoNumbersView(views.View):

    def get(self, request):
        template_name = 'calculate/math.html'
        form = MathForm()

        return render(request, template_name, {'form': form})

    def post(self, request):
        template_name = 'calculate/answer.html'
        form = MathForm(request.POST)

        if form.is_valid():
            params = form.cleaned_data
            result = math_operation.add_two_numbers(params['first'], params['second'])

            return render(request, template_name,{'result': result})