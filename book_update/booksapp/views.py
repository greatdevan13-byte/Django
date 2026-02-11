from django.shortcuts import render,redirect
from .forms import booksform
from.models import Books
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    books = Books.objects.all()
    paginator = Paginator(books, 3)  # 5 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})


def add_book(request):
    if request.method == 'POST':
        form = booksform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = booksform()

    return render(request, 'add.html', {'form': form})


def update_book(request, id):
    book  = Books.objects.get(id=id)

    if request.method == 'POST':
        form = booksform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = booksform(instance=book)

    return render(request, 'add.html', {'form': form})

def delete_book(request, id):
    book = Books.objects.get(id=id)

    book.delete()
    return redirect('home')

