from django.db import models
#from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ratio(models.Model):
  numer = models.PositiveIntegerField(blank=True)
  denom = models.PositiveIntegerField(blank=True)

class School(models.Model):
  name = models.TextField(max_length=50, blank=True)
  actCode = models.PositiveIntegerField(blank=True)
  state = models.TextField(max_length=2, blank=True)
  address = models.TextField(max_length=50, blank=True)
  website = models.TextField(max_length=50, blank=True)
  acceptanceRate = models.FloatField(max_length=4, blank=True)
  gRatio = models.ForeignKey(Ratio, on_delete=models.CASCADE, related_name ="gRatio") # gender ratio
  fsRatio = models.ForeignKey(Ratio, on_delete=models.CASCADE, related_name ="fsRatio") # factulty-student ratio
  classSize = models.PositiveIntegerField(blank=True)

class User(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  address = models.TextField(max_length=50, blank=True)
  inCollege = models.BooleanField(default=False)
  college = models.ForeignKey(School, on_delete=models.CASCADE)

  def __str__(self):
    if(self.isAdvisor):
      return self.user.first_name + " is a college student"
    return self.user.first_name + " is a high school student"

