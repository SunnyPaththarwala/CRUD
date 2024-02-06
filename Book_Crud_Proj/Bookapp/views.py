from django.shortcuts import render,redirect
from Bookapp.models import Book 

# Create your views here.
def homepage(request):
    # fetching data
    data = Book.objects.all()
    context={}
    context['books'] = data
    return render(request,"home.html",context)
def addbook(request):
    if request.method == "GET":
        return render (request,"addbook.html")
    else:    
        # fetch data
        title=request.POST['title']
        price=request.POST['price']
        author=request.POST['author']
        # insert data
        b = Book.objects.create(title=title,author=author,price=price)        
        b.save()
        # return render (request,"home.html") <------ ye empty page dega without any data -----
        return redirect("/home")    

def deletebook(request,bookid):
    b=Book.objects.filter(id=bookid)
    b.delete()
    return redirect("/home")    

def updatebook(request,bookid):
    if request.method =="GET":
        b=Book.objects.filter(id=bookid)
        context={}
        context['book']= b[0]
        return render(request,"updatedbook.html",context)
    else:
        title=request.POST['title']
        price=request.POST['price']
        author=request.POST['author']
        b=Book.objects.filter(id=bookid)
        b.update(title=title,author=author,price=price)
        return redirect("/home")   
   
    