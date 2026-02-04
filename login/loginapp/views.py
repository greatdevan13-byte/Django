from django.shortcuts import render
from .forms import LoginForm
# Create your views here.

def details(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            return render(request,'form.html',{
            'email': form.cleaned_data['email'],
            })
    else:
        form=LoginForm()

    return render(request,'index.html',{'form':form})
