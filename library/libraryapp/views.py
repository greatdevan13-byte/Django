from django.shortcuts import render
from .forms import libraryForm
from .models import library

# Create your views here.
def details(request):
    if request.method== 'POST':
        form = libraryForm(request.POST)
        if form.is_valid():
            lib= form.save()
            data= library.objects.all()
            return render(request,'forms.html',{
                'library':lib,
                'data':data
            })
    else:
        form= libraryForm()
    return render(request,'index.html',{'form':form})


   
   