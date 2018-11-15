from django.shortcuts import render
from feedback.models import Feedback



def feedbacks(request):
    fobj = Feedback.objects.all()

    return render(request, "feedbackview/feed.html", {'data': fobj})
