from django.shortcuts import render

def details(request):
    emp_details=[
        {'name':'Raj', 'jobtitle':'Cloud developer','salary':20000, 'time':True},
        {'name':'Ramu', 'jobtitle':'Software developer','salary':30000, 'time':False},
        {'name':'Rajesh', 'jobtitle':'Java developer','salary':50000, 'time':True}

    ]
    context={'emp_details':emp_details}
    return render(request,'h.html',context)

    



