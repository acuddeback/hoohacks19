from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ratio(models.Model):
    numer = models.PositiveIntegerField(null=True)
    denom = models.PositiveIntegerField(null=True)


class School(models.Model):
    name = models.TextField(max_length=50, null=True)
    actCode = models.PositiveIntegerField(null=True, unique=True)
    state = models.TextField(max_length=2, null=True)
    address = models.TextField(max_length=50, null=True)
    website = models.TextField(max_length=50, null=True)
    acceptanceRate = models.FloatField(max_length=4, null=True)
    gRatio = models.ForeignKey(
        Ratio, on_delete=models.CASCADE, related_name="gRatio")  # gender ratio
    fsRatio = models.ForeignKey(
        Ratio, on_delete=models.CASCADE, related_name="fsRatio")  # factulty-student ratio
    classSize = models.PositiveIntegerField(null=True)
    imgUrl = models.TextField(max_length=1000, null=True)


class Major(models.Model):
    name = models.TextField(max_length=50, null=True, unique=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, auto_now=True)
    inCollege = models.BooleanField(default=False)
    # college student fields,
    college = models.ForeignKey(School, on_delete=models.CASCADE)
    major = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="major", null=True)
    secondMaj = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="secondMaj", null=True)
    minor = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="minor", null=True)
    secondMin = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="secondMin", null=True)
    hometown = models.TextField(max_length=50, null=True)
    interests = models.TextField(max_length=140, null=True)
    bio = models.TextField(max_length=400, null=True)
    gradYear = models.PositiveIntegerField(null=True)

    def __str__(self):
        if(self.inCollege):
            return self.user.first_name + " is a college student"
        return self.user.first_name + " is a high school student"
