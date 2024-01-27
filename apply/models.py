from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length = 20)
    major = models.CharField(max_length = 20)
    student_id = models.CharField(max_length = 20)
    q_1 = models.TextField(default = "")
    q_2 = models.TextField(default = "")
    q_3 = models.TextField(default = "")