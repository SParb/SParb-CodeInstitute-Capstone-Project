from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import FeedbackForm
# Create your views here.


def about_text(request):
    """
    Renders the most recent information on the website author
    and allows user feedback submission.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.

    **Template**
    :template:`about/about.html`
    """
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
