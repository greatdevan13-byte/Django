from django.shortcuts import render,redirect
from .models import School
from .forms import Studentform
# Create your views here.

def add(request):
    if request.method=='POST':
        form =Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form= Studentform()
    return render(request,'home.html',{'form':form})
    
def view_students(request):
        students= School.objects.all()
        return render(request,'view_students.html', {'students':students})
    
def update_students(request,id):
        students =School.objects.get(id=id)
        if request.method=='POST':
            form =Studentform(request.POST, instance=students)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        else:
                form= Studentform(instance=students)
        return render(request,'update.html',{'form':form})
        

def delete_students(request, id):
            students =School.objects.get(id=id)
            students.delete()
            return redirect('student_list')