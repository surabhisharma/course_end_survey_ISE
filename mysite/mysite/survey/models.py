from django.db import models

class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

class sem_8(models.Model):
    usn = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    done = models.IntegerField()
    def __str__(self):
        return self.usn


class sem_6_ads(models.Model):
    usn = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    done = models.IntegerField()
    def __str__(self):
        return self.usn

class sem_6_cc(models.Model):
    usn = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    done = models.IntegerField()
    def __str__(self):
        return self.usn

class sem_4(models.Model):
    usn = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    done = models.IntegerField()
    def __str__(self):
        return self.usn

class ads(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    def __str__(self):
        return self.usn

class wp(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class cn(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class oomd(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class psq(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class cc(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class se(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class tfc(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class oop(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    def __str__(self):
        return self.usn

class ada(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    def __str__(self):
        return self.usn

class unix(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    def __str__(self):
        return self.usn


class icl(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    def __str__(self):
        return self.usn

class project(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    def __str__(self):
        return self.usn

class san(models.Model):
    usn = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    def __str__(self):
        return self.usn