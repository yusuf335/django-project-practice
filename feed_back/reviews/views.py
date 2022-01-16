from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class ReviewView(CreateView):
    model = Review
    from_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank-you"

class ThankYou(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['message'] = "This works"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "single_review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        
        context["is_favorite"] = True

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)



