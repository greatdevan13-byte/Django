from django.shortcuts import render
from .forms import LoginForm
def greeting(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'form.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = LoginForm()
    return render(request,'index.html',{'form':form})

def aboutUs(request):
    return render(request,'about.html')
def pages(request, title):
    return render(request,'pages.html',{'title':title})
def count(request, num):
    return render(request,'count.html',{'num':num})