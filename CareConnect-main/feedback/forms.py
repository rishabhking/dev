from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comments']
        widgets = {
            'rating': forms.RadioSelect(),
            'comments': forms.Textarea(attrs={'rows': 4}),
        }
