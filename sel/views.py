from django.shortcuts import render, redirect
from . import models
from . forms import Chois
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def product(request):
    last = models.Order.objects.last()
    order_id = last.id
    prod = models.Product.objects.all().order_by('Type')


    context = {
            'products': prod,
            'order':order_id,
    }
    return render(request, 'products.html', context)

def new(request):
    v=models.Order.objects.filter(value=0)
    if v.count()==0:
       models.Order.objects.create()

    return render(request,'new.html')

def Item(request,product_id):
 d1=models.Product.objects.get(id=product_id)
 d=d1.Price
 if request.method == 'GET':
     data = Chois

     return render(request, 'Item.html', {'form': data,'or':ord})

 else:
     last = models.Order.objects.last()
     order_id=last.id
     data = Chois(request.POST)

     if data.is_valid():
         table = models.Get()

         table.count = data.cleaned_data['count']
         table.product_id_id = product_id
         table.order_id_id = order_id
         c = d * data.cleaned_data['count']
         table.value = c
         table.Ch = data.cleaned_data['Ch']
         table.K = data.cleaned_data['K']
         table.M = data.cleaned_data['M']
         table.Pot = data.cleaned_data['p']
         table.Sh = data.cleaned_data['S']
         table.T = data.cleaned_data['T']

         table.save()
         res = models.Get.objects.filter(order_id=order_id).select_related()
         value = models.Order.objects.filter(id=order_id).update(state=1)
         val = res.aggregate(total=Sum('value'))
         a = (val.get('total'))
         value = models.Order.objects.filter(id=order_id).update(value=a)
         # last= models.Order.objects.last()

     return redirect('/sel/list/')

def kitchen(request):
     post1 = models.Get.objects.filter(state=0)

     orders = models.Order.objects.filter(state=1)

     d = orders
     prod = models.Get.objects.filter(order_id__in=orders, state=0)



     context = {'orders': orders, 'prod': prod}

     return render(request, 'kitchen.html', context)


def order_control(request):
    post1 = models.Get.objects.filter(state=0)

    orders = models.Order.objects.filter(state=1)

    d = orders
    prod = models.Get.objects.filter(order_id__in=orders)

    context = {'orders': orders, 'prod': prod}

    return render(request, 'order.html', context)

def done(request,order_id):
    post1 = models.Get.objects.filter(order_id_id=order_id).update(state=1)
    return redirect('/sel/kitchen/')

def doneo(request,order_id):

    post1=models.Get.objects.filter(order_id=order_id)

    post1.delete()
    post = models.Order.objects.filter(id=order_id).update(state=2)

    return redirect('/sel/order_control/')
def order_tip(request):
    return render(request, 'products.html')

def print(request,order):
    ord1 = order
    ord=models.Order.objects.get(id=order)

    inf = models.Restaurant_information.objects.get(id=1)
    post1 = models.Get.objects.filter(order_id=order).select_related()
    s=models.Get.objects.filter(order_id=order)
    m=s.count()
    if m !=0:
       context={'print':post1,'ord1':ord1,'inf':inf,'ord':ord}

       return render(request,'print.html',context)
    else:
        messages.warning(request, 'لا يوجد أصناف في هذا الطلب حالياً,فضلاً أضف الأصناف التي تريدها')  # <-
        return redirect('/sel/list/')
def cancle(request,order):

    post1=models.Get.objects.filter(order_id=order)

    post1.delete()
    post = models.Order.objects.filter(id=order).update(value=0)

    return redirect('/sel/')

@login_required
def cash(request):
    res = models.Order.objects.all()
    val = res.aggregate(total=Sum('value'))
    context={'res':res,'val':val}
    return render(request,'cash.html',context)
