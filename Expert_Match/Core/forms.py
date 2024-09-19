from django import forms
from .models import Expert, DomainExpertise, Role, Industry, Education, IndustryProject

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = [
            'name',
            'specialization_level',
            'years_of_experience',
            'publications_count',
            'previous_interview_experience_years'
        ]

class DomainExpertiseForm(forms.ModelForm):
    class Meta:
        model = DomainExpertise
        fields = ['field']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role']

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['industry']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'field', 'institute']

class IndustryProjectForm(forms.ModelForm):
    class Meta:
        model = IndustryProject
        fields = ['project']
