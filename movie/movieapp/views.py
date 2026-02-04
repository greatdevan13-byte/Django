from django.shortcuts import render

# Create your views here.
from .forms import Movieform
def details(request):
    if request.method=='POST':
        form=Movieform(request.POST)
        if form.is_valid():
            mov=form.save()
            return render(request,'form.html',{
                'message':'MOvie Saved',
                'movie':mov
            })
    else:
            form=Movieform()
    return render(request,'index.html',{'form':form})    
