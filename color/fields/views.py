from django import forms
from django.shortcuts import render
def details(request):
    if request.method== 'POST':
        name=request.POST.get('Name')
        color=request.POST.get('Color')
        return render(request,'form2.html',{
            'formData':request.POST,
            'Name':name,
            'Color':color
        })
    return render(request,'index.html')


