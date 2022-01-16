from django import forms
from django.forms import fields

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['ower_comment']
        lables = {
            'user_name': "Your Name",
            'review-text': "Your Feedback",
            'rating': "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name!"
            }
        }

