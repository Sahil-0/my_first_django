from django.shortcuts import render, get_object_or_404
from .forms import PhoneModelForm, ReviewForm
from .models import Brand, PhoneModel, Review

#Brand List (index page)
def index(request):
    brands = Brand.objects.all()
    return render(request, 'PhoneReview/index.html', {'brands': brands})

#Models by Brand
def brand_models(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    models = PhoneModel.objects.filter(brand=brand)
    return render(request, 'PhoneReview/models.html', {
        'brand': brand,
        'models': models
    })

#Model Details (Reviews + Links)
def model_detail(request, model_id):
    phone_model = get_object_or_404(PhoneModel, id=model_id)
    reviews = Review.objects.filter(models_reviewed=phone_model)

    return render(request, 'PhoneReview/detail.html', {
        'model': phone_model,
        'reviews': reviews
    })


def add_phone(request):
    if request.method == 'POST':
        form = PhoneModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PhoneModelForm()

    phones = PhoneModel.objects.all()

    return render(request, 'PhoneReview/add_phone.html', {
        'form': form,
        'phones': phones
    })

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()

    reviews = Review.objects.all()

    return render(request, 'PhoneReview/add_review.html', {
        'form': form,
        'reviews': reviews
    })