from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.http import HttpResponse

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thank you for filling the form..."
        return HttpResponse(msg)
