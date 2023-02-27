from django.db import models

# Create your models here.
COURSE_CHOICES=(
    ('python','Python'),
    ('java','Java'),
    ('c++','C++'),
    ('web design','Web Design'),
    ('dot net','Dot Net'),
    ('testing','Testing'),
    ('data science','Data Science'),
    ('data analytics','Data Analytics')
)
class Students(models.Model):
    Rollno = models.IntegerField(default="")
    Name = models.CharField(max_length=20,default="")
    Address = models.CharField(max_length=50,default="")
    Email = models.EmailField(default="")
    Mobile = models.BigIntegerField(default="")
    Course = models.CharField(max_length=20,choices=COURSE_CHOICES,default='')
