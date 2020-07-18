from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1 = dt.datetime.now()

def feedbackView(request):
    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')
            data = FeedbackData(
                name = name,
                rating = rating,
                feedback = feedback,
                date = date1
            )
            data.save()
            fform = FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request, 'feedback.html', {'fform':fform, 'feedbacks': feedbacks})
        else:
            return HttpResponse('Invalid Data')
    else:
        fform = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request, 'feedback.html', {'fform':fform, 'feedbacks': feedbacks})