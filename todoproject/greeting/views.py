from django.shortcuts import render

def greeting(request):
    if request.GET:
        username = request.GET.get('username')

        return render(request, 'form-data.html', {
            'username': username,
            'formData': request.GET
        })

    return render(request, 'index.html')