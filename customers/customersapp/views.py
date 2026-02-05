from django.shortcuts import render

# Create your views here.
from .forms import customerform
from .models import customers

def details(request):
    if request.method=='POST':
        form= customerform(request.POST)
        if form.is_valid():
            cust=form.save()
            data= customers.objects.all().order_by('name')
            return render(request,'all.html',{
                'data':data,
                'customer':cust
            })
    else:
        form=customerform()
        return render(request,'index.html',{'form':form})
    
def filtered(request):
    data=customers.objects.filter(email__endswith= '@example.com') 
    return render(request,'filtered.html',{
        'data':data
    })
