from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from .forms import productForm
from .models import Product
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def add_details(request):
    if request.method=='POST':
        form=productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    else:
            form=productForm()
    return render(request, 'form.html',{'form':form})


def view_product(request):
     product= Product.objects.all()
     return render(request, 'product_details.html',{'product':product})



def generate_pdf(request,pk):
     product= get_object_or_404(Product,pk=pk)
     template= get_template('product_pdf.html')
     html= template.render({'product':product})

     buffer=BytesIO()

     pisa_status= pisa.CreatePDF(html, dest=buffer)

     if pisa_status.err:
          return HttpResponse('PDF generation error!')
     else:
          response = HttpResponse(buffer.getvalue(),content_type='application/pdf')
          response['Content-Disposition']= 'attachment; filename="{}.pdf"'.format(product.name)
          return response