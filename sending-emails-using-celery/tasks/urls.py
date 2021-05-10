from django.urls import path
from tasks.views import ReviewEmailView

urlpatterns = [
    path('reviews/', ReviewEmailView.as_view(), name='reviews')
]