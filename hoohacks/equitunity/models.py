from django.db import models
# Create your models here.
class User(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  address = models.TextField(max_length=50, blank=True)
  inCollege = models.BooleanField(default=False)

  def __str__(self):
    if(self.isAdvisor):
      return self.user.first_name + " is a college student"
    return self.user.first_name + " is a high school student"

class School(models.Model):
  name = models.TextField(max_length=50, blank=True)
  actCode = models.PositiveIntegerField(max_length=6, blank=True)
  state = models.TextField(max_length=2, blank=True)
  address = models.TextField(max_length=50, blank=True)
  website = models.TextField(max_length=50, blank=True)
  acceptanceRate = models.FloatField(max_length=4, blank=True)



