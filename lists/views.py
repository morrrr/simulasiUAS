from django.shortcuts import redirect, render
from lists.models import Item, List
import random

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list':list_})

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    
    angkaRandom = random.randint(1,30)
    angkaTebakan = int(request.POST['item_text'])    
    
    item=Item()
    item.angka = angkaRandom
    item.tebakan = angkaTebakan
    item.status = lihatStatus(angkaRandom, angkaTebakan)
    item.list = list_
    item.save()
    
    return redirect('/lists/%d/' % (list_.id,))
    
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    angkaRandom = random.randint(1,30)
    angkaTebakan = int(request.POST['item_text'])    
    
    item=Item()
    item.angka = angkaRandom
    item.tebakan = angkaTebakan
    item.status = lihatStatus(angkaRandom, angkaTebakan)
    item.list = list_
    item.save()

    return redirect('/lists/%d/' % (list_.id,))

def lihatStatus(angka, tebakan):
    if tebakan<angka+2 and tebakan>angka-2:
    	return 'Kamu menang!!'
    else:
        return 'Kamu kalah...'
