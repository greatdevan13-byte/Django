from django.shortcuts import render

def user(request):
    if request.GET:
        username=request.GET.get('username')
        return render(request,'form.html',{
            'formData':request.GET,
            'username':username
        })
    return render(request,'index.html')

