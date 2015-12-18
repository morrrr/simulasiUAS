from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item, List

from lists.views import home_page

class ListViewTest(TestCase):
    # nomor b
    def test_displays_items_to_web(self):
        correct_list = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=correct_list)
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertContains(response, 'Kamu menang!!')
    
    # nomor e
    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=correct_list)
        
        other_list = List.objects.create()
        Item.objects.create(angka=15, tebakan=10, status='Kamu kalah...',list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))
        response2 = self.client.get('/lists/%d/' % (other_list.id,))

        self.assertContains(response, 'Kamu menang!!')
        self.assertNotContains(response, 'Kamu kalah...')
    
    # nomor c
    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)
        
class NewListTest(TestCase):
    # nomor a
    def test_record_game_to_database(self):
        a_list = List.objects.create()
        Item.objects.create(angka=10, tebakan=9, status='Kamu menang!!', list=a_list)

        self.assertEqual(Item.objects.count(), 1)

class NewItemTest(TestCase):
    # nomor d
    def test_record_second_third_etc_game(self):
        list_nya = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=list_nya)
        a = self.client.post(
            '/lists/%d/add_item' % (list_nya.id,),
            data={'item_text': '17'}
        )
        response = self.client.get('/lists/%d/' % (list_nya.id))
        self.assertEqual(Item.objects.count(),2)
        self.assertContains(response, 'Tebakan :15,')
        self.assertContains(response, 'Tebakan :17,')
        #self.fail(response)

class ListAndItemModelTest(TestCase):
    # test komentar tiap x kali menang
    def test_comment_no_win(self):
        list_nya = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=list_nya)

        response = self.client.get('/lists/%d/' % (list_nya.id))
        self.assertNotContains(response, 'Ulala!!')
        self.assertNotContains(response, 'Ulalala')
        self.assertNotContains(response, 'Uulala')

    def test_comment_three_win(self):
        list_nya = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        response = self.client.get('/lists/%d/' % (list_nya.id))
        self.assertContains(response, 'Ulala!!')
        self.assertNotContains(response, 'Ulalala')
        self.assertNotContains(response, 'Uulala')

    def test_comment_five_win(self):
        list_nya = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        response = self.client.get('/lists/%d/' % (list_nya.id))
        self.assertNotContains(response, 'Ulala!!')
        self.assertContains(response, 'Ulalala')
        self.assertNotContains(response, 'Uulala')

    def test_comment_ten_win(self):
        list_nya = List.objects.create()
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=15, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=14, status='Kamu menang!!',list=list_nya)
        Item.objects.create(angka=15, tebakan=16, status='Kamu menang!!',list=list_nya)
        response = self.client.get('/lists/%d/' % (list_nya.id))
        self.assertNotContains(response, 'Ulala!!')
        self.assertNotContains(response, 'Ulalala')
        self.assertContains(response, 'Uulala')
