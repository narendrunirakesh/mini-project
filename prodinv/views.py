from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import product_adding
from django.contrib import messages

from .forms import ProductForm

# Create your views here.    
    
def homepage(request):
    return render(request,'home.html')

def createproduct(request):
    if request.method=='POST':
        prodid=int(request.POST['prodid'])
        prodname=request.POST['prodname']
        prodcategory=request.POST['prodcategory']
        prodprice=float(request.POST['prodprice'])
        
       # obj= product_adding(product_id=prodid,product_name=prodname,product_category=prodcategory,product_price=prodprice)
        #obj.save()
        product_adding.objects.create(product_id=prodid,product_name=prodname,product_category=prodcategory,product_price=prodprice)
        
        messages.success(request,'data saved')
        
        #return HttpResponse('data saved success')
        
    return render(request,'create.html')

def readproduct(request):
    context={}
    emprecords=product_adding.objects.all
    context['emprecords']=emprecords
    
    return render(request,'read.html',context)


def deleteproduct(request):
    context={}
    if request.method == 'POST':
        prodid=int(request.POST['prodid'])
        rec=product_adding.objects.get(product_id=prodid)
        context['record']=rec
        return render(request,'alert.html',context)        
    return render(request,'delete.html')

def deleteprodid(request,prodid):
    prodid=product_adding.objects.get(product_id=prodid)
    prodid.delete()
    
    return render(request,'delete.html')


    
def updateproduct(request,prodid):
    item=get_object_or_404(product_adding,pk=prodid)
    if request.method=='POST':
        prodid=int(request.POST.get('prodid'))
        prodname=request.POST.get('prodname')
        prodcategory=request.POST.get('prodcategory')
        prodprice=float(request.POST.get('prodprice'))
        
        item.prodid=prodid
        item.prodname=prodname
        item.prodcategory=prodcategory
        item.prodprice=prodprice
        item.save()
        print('------',item)
        return HttpResponse('updated successfully')
    else:
        return render(request,'update.html',{'item':item})
    
            
def updateproduct(request, prodid):
    prodid = get_object_or_404(product_adding, product_id=prodid)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=prodid)
        if form.is_valid():
            form.save()
            return redirect('createurl')  # Redirect to product list or another page after updating
    else:
        form = ProductForm(instance=prodid)
    return render(request, 'product_form.html', {'form': form})  
        
        
        