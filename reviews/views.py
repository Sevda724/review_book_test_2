from django.shortcuts import render, redirect
from reviews.forms import ReviewForm
from django.shortcuts import redirect
from reviews.models import Review
from django.views import View


# Create your views here.
class ReviewsView(View):
    def get(self, request):
        form=ReviewForm()
        reviews = Review.objects.all()
        return render(request,'reviews.html',{'form':form,'reviews':reviews})

    def post(self, request):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                name = data.get('name')
                email = data.get('email')
                review = data.get('review')
                rating = data.get('rating')
                Review.objects.create(name=name, email=email, review=review, rating=rating)

                return redirect('reviews')

        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})

def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            Review.objects.create(name=name, email=email, review=review, rating=rating)

            return redirect('reviews')

    form = ReviewForm()
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'form': form,'reviews':reviews})




def reviews_old_2(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            Review.objects.create(name=name, email=email, review=review, rating=rating)

            return redirect('reviews')

    form = ReviewForm()
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'form': form,'reviews':reviews})


def reviews_old(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'reviews.html', {'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')

            Review.objects.create(name=name, email=email, review=review, rating=rating)
            # with open('data.csv','a') as file:
            #     file.write(f'{name}|{email}|{review}|{rating}\n')

            return redirect('reviews')
            # name_1 = request.GET.get('name')
            # email_1=request.GET.get('email')
            # review_1=request.GET.get('review')
            # return render(request,'reviews.html',{'name_1':name_1,'email_1':email_1,'review_1':review_1,'form':form})
    else:
        form = ReviewForm()
        return render(request, 'reviews.html', {'form': form})