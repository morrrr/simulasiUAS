from django.shortcuts import redirect, render
from lists.models import Item, List
import random

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    comment = insert_comment(list_)
    return render(request, 'list.html', {'list':list_, 'comment':comment})

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

def insert_comment(list_periksa):
    list_temp = Item.objects.filter(list=list_periksa).reverse()
    counter = 0
    comment = ''

    if len(list_temp)<3:
        return comment

    for i in range(3):
        item=list_temp[i]
        if item.status == 'Kamu menang!!':
            counter = counter+1

    if counter == 3:
        comment = 'Ulala!!'

    if len(list_temp)<5:
        return comment

    counter = 0

    for i in range(5):
        item = list_temp[i]
        if item.status == 'Kamu menang!!':
            counter = counter+1

    if counter == 5:
        comment = 'Ulalala'

    if len(list_temp)<10:
        return comment

    counter = 0

    for i in range(10):
        item = list_temp[i]
        if item.status == 'Kamu menang!!':
            counter = counter+1

    if counter == 10:
        comment = 'Uulala'

    return comment