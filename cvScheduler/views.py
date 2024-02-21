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
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        degree = request.POST.get('degree')
        degree1 = request.POST.get('degree1')
        degree2 = request.POST.get('degree2')
        passing_year = request.POST.get('passing_year')
        passing_year1 = request.POST.get('passing_year1')
        passing_year2 = request.POST.get('passing_year2')
        result = request.POST.get('result')
        result1 = request.POST.get('result1')
        result2 = request.POST.get('result2')
        objectives = request.POST.get('objectives')
        experience = request.POST.get('workExperience')
        skills = request.POST.get('skills')
        if image:
            some = CvInfo.objects.create(fullName=name, email=email, phone=phone, gender=gender, religion=religion, address=address, image=image, degree=degree, degree1=degree1, degree2=degree2, passing_year=passing_year, passing_year1=passing_year1,passing_year2=passing_year2,result=result, result1=result1, result2=result2, workExperience=experience, objectives=objectives, skills=skills)
            some.save()
            messages.success(request, 'Successfully Added')
        else:
            some = CvInfo.objects.create(fullName=name, email=email, phone=phone, gender=gender, religion=religion, address=address, degree=degree, degree1=degree1, degree2=degree2, passing_year=passing_year, passing_year1=passing_year1,passing_year2=passing_year2,result=result, result1=result1, result2=result2, workExperience=experience, objectives=objectives, skills=skills)
            some.save()
            messages.success(request, 'Successfully Added')
    return render(request, 'cv/home.html')

def profile(request):
    cv = CvInfo.objects.all()
    return render(request, 'cv/profile.html', locals())

def view_profile(request,id):
    cv = CvInfo.objects.get(id=id)
    return render(request, 'cv/viewprofile.html', locals())

def delete_schedule(request, id):
    sc = Scheduler.objects.get(id=id)
    sc.delete()
    return redirect('schedule/view_schedule')
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
    return render(request, 'schedule/updateSchedule.html', locals())

def schedule(request):
    if request.method == 'POST':
        scheduleName = request.POST.get('scheduleName')
        scheduleDate = request.POST.get('scheduleDate')
        scheduleTime = request.POST.get('scheduleTime')

        sc = Scheduler.objects.create(scheduleName=scheduleName, scheduleDate=scheduleDate, scheduleTime=scheduleTime)
        sc.save()
    return render(request, 'schedule/scedule.html')

def viewSchedule(request):
    sc = Scheduler.objects.all()
    return render(request, 'schedule/viewSchedule.html', locals())
def resume(request, id):
    user_profile = CvInfo.objects.get(id=id)
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('viewprofile', args=[id])), output_path=False,configuration=config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content_Disposition'] = 'attachment; filename="file_name.pdf"'
    return response