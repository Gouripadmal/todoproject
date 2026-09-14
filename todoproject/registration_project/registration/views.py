
from django.shortcuts import render
from .forms import LoginForm
def greeting(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'form-data.html',{
                'email': form['email'].value
            })
    return render(request,'index.html')
