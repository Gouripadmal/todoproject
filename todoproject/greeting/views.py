from django.shortcuts import render

def employees(request):

    employee_list = [
        {
            'name': 'John',
            'job_title': 'Software Developer',
            'salary': 50000,
            'full_time': True
        },
        {
            'name': 'Anu',
            'job_title': 'UI Designer',
            'salary': 40000,
            'full_time': False
        },
        {
            'name': 'Rahul',
            'job_title': 'Project Manager',
            'salary': 70000,
            'full_time': True
        }
    ]

    return render(request, 'employees.html', {
        'employees': employee_list
    })