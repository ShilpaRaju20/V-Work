from django.shortcuts import render
from complaint.models import Complaint


def complaints(request):
    cobj = Complaint.objects.all()

    return render(request, "complaintview/complaint.html", {'data': cobj})

