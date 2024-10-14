from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuse

@login_required
@user_passes_test(is_admin)

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback:submit_feedback')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})

def view_feedback(request):
    # Only retrieve feedback submitted by the logged-in user
    feedback_list = Feedback.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'feedback/view_feedback.html', {'feedback_list': feedback_list})
