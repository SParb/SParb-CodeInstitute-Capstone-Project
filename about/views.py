from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import FeedbackForm
# Create your views here.

def about_me(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.add_message(request, messages.SUCCESS, "Feedback request received! I endeavour to respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    feedback_form = FeedbackForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "feedback_form": feedback_form},
    )