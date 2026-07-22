
    
from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User

class User(AbstractUser):

    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('candidate', 'Candidate'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)



# Employer

class Employer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='employer'
    )

    company_name = models.CharField(max_length=200)
    company_email = models.EmailField()
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name



# Candidate

class Candidate(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='candidate'
    )

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    experience = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.full_name

class Job(models.Model):

    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -----------------------
# Application
# -----------------------
class Application(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.full_name} - {self.job.title}"