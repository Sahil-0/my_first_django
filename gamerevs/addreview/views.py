from django.shortcuts import render
from django.views import generic
from .forms import ReviewForm
from gamereview.models import Review
from django.http import HttpResponseRedirect
from django.urls import reverse


class AddReviewFormView(generic.TemplateView):
    template_name = 'addreview/addreviewform.html'

    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'reviews': reviews
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gamereview:gamelist'))

        reviews = Review.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'reviews': reviews
        })