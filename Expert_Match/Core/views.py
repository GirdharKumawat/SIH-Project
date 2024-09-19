from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Expert, DomainExpertise, Role, Industry, Education, IndustryProject
# import messages
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password1, first_name=name)
                    user.save()
                    # Automatically log the user in after successful signup
                    user = authenticate(request, username=username, password=password1)
                    if user is not None:
                        login(request, user)  # Logs the user in
                        return redirect('home')  # Redirect to home page
                except ValidationError as e:
                    messages.error(request, f"Error creating account: {e}")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'signup.html')

@login_required(login_url='userLogin')
def home(request):
    return render(request, 'index.html')  

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    messages.success(request,'Logout Successfull.....')
    return redirect('userLogin') 

def candidates(request):
    return render(request,'candidates.html')

def expert(request):
    experts = Expert.objects.all().prefetch_related(
        'education',
        'domain_expertise',
        'roles',
        'industries',
        'industry_projects'
    )
    return render(request, 'expert.html', {'experts': experts})

def add_expert(request):
    if request.method == 'POST':
        # Save the Expert model
        name = request.POST.get('name')
        specialization_level = request.POST.get('specialization_level')
        years_of_experience = request.POST.get('years_of_experience')
        publications_count = request.POST.get('publications_count')
        previous_interview_experience_years = request.POST.get('previous_interview_experience_years')
       

        expert = Expert.objects.create(
            name=name,
            specialization_level=specialization_level,
            years_of_experience=years_of_experience,
            publications_count=publications_count,
            previous_interview_experience_years=previous_interview_experience_years,
            
        )

        # Save Domain Expertise
        domain_expertise_fields = request.POST.get('domain_expertise', '').split(',')
        for field in domain_expertise_fields:
            DomainExpertise.objects.create(expert=expert, field=field.strip())

        # Save Roles
        roles = request.POST.get('roles', '').split(',')
        for role in roles:
            Role.objects.create(expert=expert, role=role.strip())

        # Save Industries
        industries = request.POST.get('industries', '').split(',')
        for industry in industries:
            Industry.objects.create(expert=expert, industry=industry.strip())

        # Save Education
        Education.objects.create(
            expert=expert,
            degree=request.POST.get('bachelor_degree', ''),
            field=request.POST.get('bachelor_field', ''),
            institute=request.POST.get('bachelor_institute', '')
        )
        Education.objects.create(
            expert=expert,
            degree=request.POST.get('master_degree', ''),
            field=request.POST.get('master_field', ''),
            institute=request.POST.get('master_institute', '')
        )
        Education.objects.create(
            expert=expert,
            degree=request.POST.get('phd_degree', ''),
            field=request.POST.get('phd_field', ''),
            institute=request.POST.get('phd_institute', '')
        )

        # Save Industry Projects
        industry_projects = request.POST.get('industry_projects', '').split(',')
        for project in industry_projects:
            IndustryProject.objects.create(expert=expert, project=project.strip())

        return redirect('expert')  # Redirect to a success page or another view
    else:
        return render(request, 'add_expert.html')

def add_candidate(request):
   
    return render(request,'add_candidate.html')

def match(request,pk):
    return render(request,'match.html')