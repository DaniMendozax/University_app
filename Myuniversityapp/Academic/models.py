from django.db import models

# Create your models here.

class Race(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duration: {1} year(s))"
        return txt.format(self.name, self.duration)

class Student(models.Model):
    nic = models.CharField(max_length=8, primary_key=True)
    paternal_Surname = models.CharField(max_length=35)
    mothers_surname = models.CharField(max_length=35)
    names = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    genres = [
        ('F', 'Feminine'),
        ('M', 'masculine')
    ]
    genre = models.CharField(max_length=1, choices=genres, default='F')
    race = models.ForeignKey(Race, null=False, blank=False, on_delete=models.CASCADE)
    validity = models.BooleanField(default=True)

    def fullName(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.paternal_Surname, self.mothers_surname, self.names)

    def __str__(self):
        txt = "{0} / Race: {1} / {2}"
        if self.validity:
            studentStatus = "In Force"
        else:
            studentStatus = "Down"
        return txt.format(self.fullName(), self.race, studentStatus)

class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credit = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Teacher: {2}"
        return txt.format(self.name, self.code, self.teacher)

class Registration(models.Model):
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    date_of_registrations = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        txt = "{0} / enrolled in the course {1} / Date: {2}"
        date_Register = self.date_of_registrations.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.student.fullName(), self.course, date_Register)


