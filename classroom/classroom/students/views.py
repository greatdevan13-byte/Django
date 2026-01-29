from django.shortcuts import render


def student(request):
    details=[
         {'name':'Sudheesh','grade':'C','result':False},
         {'name':'Ramesh','grade':'A','result':True},
         {'name':'Sumesh','grade':'B','result':True},
         {'name':'Sheetal','grade':'C','result':False}
    ]
    context={'details':details}
    return render(request,'stud.html',context)