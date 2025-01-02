""" create leads and agent models  """


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Source(models.TextChoices):
    YOUTUBE = ("you","Youtube")
    Google = ("go","Google")
    NEWSLETTER = ("new","NewsLetter")


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    source = models.CharField(max_length=10, choices = Source.choices)
    special_files = models.FileField(null=True, blank=True)
    agent = models.ForeignKey("Agent",on_delete = models.SET_NULL, null=True, related_name="leads")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return str(self.fullname)

class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)    
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return f"{self.user.email}"

    
    