from pickle import NONE
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from movies.models import Book
#from .forms import ReviewForm, RatingForm 
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render, get_object_or_404, redirect


def product_detail(request, id):
    print("asdhgadshsdh",id)
    book = get_object_or_404(Book, pk=id)
    print(book)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        print("TEST: \n\n\n", review_form)
        rating_form = RatingForm(request.POST)

        if review_form.is_valid() and rating_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()

            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.book = book
            rating.save()

            return redirect('product_detail', product_id=id)
    else:
        review_form = ReviewForm()
        rating_form = RatingForm()

    return render(request, 'product.html', {'book': book, 'review_form': review_form, 'rating_form': rating_form})

