from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError, models
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from .models import Patients
from .forms import PatientForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            }) 
        else:
            login(request, user)
            return redirect('patients')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username= request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('patients')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'error': 'Username is already existes'
                })
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Password do not match'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('home')    
        


def aboutus(request):
    return render(request, 'aboutus.html')

@login_required
def patients(request):
    search = request.GET.get('search')
    patient_query = Patients.objects.filter(user=request.user)
    if search:
        patient_query = patient_query.filter(
                Q(first_name__icontains = search) |
                Q(last_name__icontains = search) |
                Q(email__icontains = search) |
                Q(phone__icontains = search)).distinct()
        
    paginator = Paginator(patient_query, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
        
    return render(request, 'patients.html', {
        'patients':page_obj
    })

@login_required
def patient_detail(request, id):
    patient = get_object_or_404(Patients, pk=id, user=request.user)
    return render(request, 'patient_detail.html', {
        'patients': patient
    })
@login_required
def edit_patient(request, patient_id):
    if request.method == 'GET':
        patient = get_object_or_404(Patients, pk=patient_id, user=request.user)
        form = PatientForm(instance=patient)
        return render(request, 'edit_patient.html',{
            'patient': patient,
            'form': form
        })
    else:
        patient = get_object_or_404(Patients, pk=patient_id, user=request.user)
        form = PatientForm(request.POST, instance=patient)
        form.save()
        return redirect('patients')
@login_required
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patients, pk=patient_id, user=request.user)
    if request.method == 'GET':
        patient.delete()
        return redirect('patients')
@login_required
def createPatient(request):
    if request.method == 'GET':
        return render(request, 'create_patient.html', {
            'form': PatientForm
        })
    else:
        try:
            form = PatientForm(request.POST)
            new_patient = form.save(commit=False)
            new_patient.user = request.user
            new_patient.save()
            return redirect('patients')
        except ValueError:
            return render(request, 'create_patient.html',{
                'form': PatientForm,
                'error': 'Please provide valide data'
            })
        