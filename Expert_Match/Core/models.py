from django.db import models

class Expert(models.Model):
    SPECIALIZATION_LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ]

    name = models.CharField(max_length=255)
    specialization_level = models.CharField(max_length=50, choices=SPECIALIZATION_LEVELS)
    years_of_experience = models.PositiveIntegerField()
    publications_count = models.PositiveIntegerField()
    previous_interview_experience_years = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class DomainExpertise(models.Model):
    expert = models.ForeignKey(Expert, related_name='domain_expertise', on_delete=models.CASCADE)
    field = models.CharField(max_length=255)

    def __str__(self):
        return self.field

class Role(models.Model):
    expert = models.ForeignKey(Expert, related_name='roles', on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

class Industry(models.Model):
    expert = models.ForeignKey(Expert, related_name='industries', on_delete=models.CASCADE)
    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.industry

class Education(models.Model):
    DEGREE_CHOICES = [
        ('BSc', 'Bachelor of Science'),
        ('MSc', 'Master of Science'),
        ('PhD', 'Doctor of Philosophy'),
    ]
    
    expert = models.ForeignKey(Expert, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=10, choices=DEGREE_CHOICES)
    field = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.degree} in {self.field} from {self.institute}"

class IndustryProject(models.Model):
    expert = models.ForeignKey(Expert, related_name='industry_projects', on_delete=models.CASCADE)
    project = models.CharField(max_length=255)

    def __str__(self):
        return self.project
