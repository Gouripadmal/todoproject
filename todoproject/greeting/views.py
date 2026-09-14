from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            return render(request, 'form-data.html', {
                'email': form.cleaned_data['email']
            })
    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form})