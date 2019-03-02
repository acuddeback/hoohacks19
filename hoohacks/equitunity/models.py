from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ratio(models.Model):
    numer = models.PositiveIntegerField(blank=True)
    denom = models.PositiveIntegerField(blank=True)


class School(models.Model):
    name = models.TextField(max_length=50, blank=True)
    actCode = models.PositiveIntegerField(blank=True, unique=True)
    state = models.TextField(max_length=2, blank=True)
    address = models.TextField(max_length=50, blank=True)
    website = models.TextField(max_length=50, blank=True)
    acceptanceRate = models.FloatField(max_length=4, blank=True)
    gRatio = models.ForeignKey(
        Ratio, on_delete=models.CASCADE, related_name="gRatio")  # gender ratio
    fsRatio = models.ForeignKey(
        Ratio, on_delete=models.CASCADE, related_name="fsRatio")  # factulty-student ratio
    classSize = models.PositiveIntegerField(blank=True)
    imgUrl = models.TextField(max_length=300, blank=True)


class Major(models.Model):
    name = models.TextField(max_length=50, blank=True, unique=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inCollege = models.BooleanField(default=False)
    # college student fields,
    college = models.ForeignKey(School, on_delete=models.CASCADE)
    major = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="major")
    secondMaj = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="secondMaj")
    minor = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="minor")
    secondMin = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="secondMin")
    hometown = models.TextField(max_length=50, blank=True)
    interests = models.TextField(max_length=140, blank=True)
    bio = models.TextField(max_length=400, blank=True)
    gradYear = models.PositiveIntegerField(blank=True)

    def __str__(self):
        if(self.inCollege):
            return self.user.first_name + " is a college student"
        return self.user.first_name + " is a high school student"
