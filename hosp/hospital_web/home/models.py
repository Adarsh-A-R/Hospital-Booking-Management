from django.db import models


# Create your models here.
class Departments(models.Model):
    def __str__(self):
        return self.dep_name
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()


class Doctors(models.Model):
    def __str__(self):
        return 'Dr ' + self.doc_name + ' (' + self.doc_spec + ')'
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors_img')


class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
