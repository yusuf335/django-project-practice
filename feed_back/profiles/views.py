from django.views.generic import CreateView,ListView

from .models import UserProfile
from  reviews.models import Review

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = '__all__'
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

class ReviewsListView(ListView):
    template_name = "profiles/user_profiles.html"
    model = Review
    context_object_name = "reviews"
    