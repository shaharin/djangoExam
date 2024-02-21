from django.db import models

class CvInfo(models.Model):
    fullName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=12, null=True, blank=True)
    religion = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    degree = models.TextField(max_length=150, null=True, blank=True)
    degree1 = models.TextField(max_length=150, null=True, blank=True)
    degree2 = models.TextField(max_length=150, null=True, blank=True)
    passing_year = models.TextField(max_length=150, null=True, blank=True)
    passing_year1 = models.TextField(max_length=150, null=True, blank=True)
    passing_year2 = models.TextField(max_length=150, null=True, blank=True)
    result = models.TextField(max_length=150, null=True, blank=True)
    result1 = models.TextField(max_length=150, null=True, blank=True)
    result2 = models.TextField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='def.jpg', null=True, blank=True)
    workExperience = models.TextField(max_length=200, null=True, blank=True)
    objectives = models.TextField(max_length=200, null=True, blank=True)
    skills = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fullName

class Scheduler(models.Model):
    scheduleName = models.CharField(max_length=50)
    scheduleDate = models.CharField(max_length=50)
    scheduleTime = models.CharField(max_length=12)

    def __str__(self):
        return self.scheduleName

