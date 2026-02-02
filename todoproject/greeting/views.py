from django.shortcuts import render
def greeting(request):
    if request.GET:
     email = request.GET.get('email')
     password=request.GET.get('passwordssss')
     return render(request,'form.html',{
         'formData':request.GET,
         'email': email
     })
    return render(request,'index.html')