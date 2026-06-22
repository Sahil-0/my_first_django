from django.shortcuts import render, get_object_or_404,redirect
from .forms import PhoneModelForm, ReviewForm, UserForm
from .models import Brand, PhoneModel, Review
from django.contrib.auth import authenticate, login, mixins
from django.contrib.auth.decorators import login_required
from django.views import generic

#Brand List (index page)
def index(request):
    brands = Brand.objects.all()

    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits

    return render(request, 'PhoneReview/index.html', {
        'brands': brands,
        'visits': visits
    })

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

@login_required(login_url='/register/')
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

@login_required(login_url='/register/')
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

class AddUserFormView(generic.TemplateView):
    template_name = 'PhoneReview/registrationform.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

        return render(request, self.template_name, {'form': form})