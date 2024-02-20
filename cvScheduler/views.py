from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from cvScheduler.models import CvInfo, Scheduler
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
# Create your views here.
def home(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        education = request.POST.get('education')
        workExperience = request.POST.get('workExperience')
        skills = request.POST.get('skills')
        if image:
            some = CvInfo.objects.create(fullName=fullName, email=email, phone=phone, image=image, education=education, workExperience=workExperience, skills=skills)
            some.save()
            messages.success(request, 'Successfully Added')
        else:
            some = CvInfo.objects.create(fullName=fullName, email=email, phone=phone, image=image, education=education,
                                         workExperience=workExperience, skills=skills)
            some.save()
            messages.success(request, 'Successfully Added')
    return render(request, 'home.html')

def profile(request):
    cv = CvInfo.objects.all()
    return render(request, 'profile.html', locals())

def view_profile(request,id):
    cv = CvInfo.objects.get(id=id)
    return render(request, 'viewprofile.html', locals())

def delete_schedule(request, id):
    sc = Scheduler.objects.get(id=id)
    sc.delete()
    return redirect('view_schedule')
def update_schedule(request, id):
    sc = Scheduler.objects.get(id=id)
    if request.method == 'POST':
        scheduleName = request.POST.get('scheduleName')
        scheduleDate = request.POST.get('scheduleDate')
        scheduleTime = request.POST.get('scheduleTime')
        sc.scheduleName = scheduleName
        sc.scheduleDate = scheduleDate
        sc.scheduleTime = scheduleTime
        sc.save()
        return redirect('view_schedule')
    return render(request, 'updateSchedule.html', locals())

def schedule(request):
    if request.method == 'POST':
        scheduleName = request.POST.get('scheduleName')
        scheduleDate = request.POST.get('scheduleDate')
        scheduleTime = request.POST.get('scheduleTime')

        sc = Scheduler.objects.create(scheduleName=scheduleName, scheduleDate=scheduleDate, scheduleTime=scheduleTime)
        sc.save()
    return render(request, 'scedule.html')

def viewSchedule(request):
    sc = Scheduler.objects.all()
    return render(request, 'viewSchedule.html', locals())
def resume(request, id):
    user_profile = CvInfo.objects.get(id=id)
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('viewprofile', args=[id])), output_path=False,configuration=config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content_Disposition'] = 'attachment; filename="file_name.pdf"'
    return response