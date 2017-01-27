from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from lifion.models import Organization, LifionUser


def index(request):
    if request.user.is_authenticated:
        pass

    return render(request, 'lifion/index.html')


def record_response(request, survey_id):
    pass


def manage_question_bank(request):
    pass


def register(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged Out!')
    return redirect('employees')


def manage_organizations(request):
    if request.method == 'POST':

        action = request.POST.get('action')

        if action == 'add':
            name = request.POST.get('name')

            organization = Organization.objects.create(name=name)

        elif action == 'delete':
            id = request.POST.get('id')

            organization = Organization.objects.get(id=id)
            organization.delete()

    orgs = Organization.objects.all()
    return render(request, 'lifion/organizations.html', {
        'organizations': orgs,
        'orgs': True
    })


def manage_employees(request):
    if request.method == 'POST':

        action = request.POST.get('action')

        if action == 'add':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            organization_id = request.POST.get('organization')

            user = LifionUser.objects.filter(username=username).first()

            if user is None:
                organization = Organization.objects.get(id=organization_id)

                user = LifionUser.objects.create(username=username,
                                                 first_name=first_name,
                                                 last_name=last_name,
                                                 organization=organization)

                user.set_password('pass@123')
                user.save()
                messages.success(request, 'Successfully registered {}'.format(username))
            else:
                messages.error(request, 'User already exists. Please try with a different Username.')

        elif action == 'login':
            emp_id = request.POST.get('emp_id')

            user = LifionUser.objects.get(id=emp_id)

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            messages.success(request, 'Logged In as {} {}'.format(user.first_name, user.last_name))
            login(request, user)

    if not request.user.is_authenticated:
        orgs = Organization.objects.all()
        return render(request, 'lifion/employees.html', {
            'organizations': orgs,
            'emps': True
        })
    return redirect('home')
