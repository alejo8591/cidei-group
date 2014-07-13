from django.test import TestCase
from sales.models import Categories, OrderDetail, Orders, Products, Suppliers
from django.conf import settings
from django.core.files import File
import os

class TestSales(TestCase):
	def setUp(self):
		""" Create Categories """
		# for picture use http://placehold.it/200x200 and http://placehold.it/350x200
		self.category_one =  Categories.objects.create(name='Software', description='Test Software', picture=File(open(os.path.join(settings.TEST_IMAGES_SALES_APP, '200x200.gif'))))
		self.category_two =  Categories.objects.create(name='Hardware', description='Test Hardware', picture=File(open(os.path.join(settings.TEST_IMAGES_SALES_APP, '350x200.gif'))))
		self.category_three =  Categories.objects.create(name='Food', description='Test Food', picture=None)
		# Suppliers Model
		self.supplier_one = Suppliers.objects.create(name="Ominia", description="Omnia sunt communia", address="Kr 20 20 20", phone="1234567")
		self.supplier_two = Suppliers.objects.create(name="Dedis", description="Omnia sunt", address="Kr 30 20 20", phone="123456798")

		# Delete test image
		pictures = [p for p in os.listdir(os.path.join(settings.MEDIA_ROOT, 'images/')) if p.endswith(".gif")]
		for p in pictures:
			os.remove(os.path.join(settings.MEDIA_ROOT, 'images/')+p)

	def test_category_one(self):
		cat_one = Categories.objects.get(name="Software")
		self.assertEqual(cat_one.description, 'Test Software')
		self.assertEqual(cat_one.picture.path, unicode(os.path.join(settings.MEDIA_ROOT, 'images/200x200.gif')))

	def test_category_two(self):
		cat_two = Categories.objects.get(name="Hardware")
		self.assertEqual(cat_two.description, 'Test Hardware')
		self.assertEqual(cat_two.picture.path, unicode(os.path.join(settings.MEDIA_ROOT, 'images/350x200.gif')))

	def test_category_three(self):
		try:
			cat_three = Categories.objects.get(name="Food")
			self.assertEqual(cat_three.description, 'Test Food')
			self.assertEqual(cat_three.picture.path, unicode(os.path.join(settings.MEDIA_ROOT, 'images/350x200.gif')))
		except:
			print "File not found"

	def test_supplier_one_and_two(self):
		supplier_one = Suppliers.objects.get(name="Ominia")
		supplier_two = Suppliers.objects.get(name="Dedis")
		self.assertEqual(supplier_one.description, 'Omnia sunt communia')
		self.assertEqual(supplier_two.description, 'Omnia sunt')
		self.assertNotEqual(supplier_one.description, supplier_two.description)
		self.assertEqual(supplier_one.address, unicode('Kr 20 20 20'))
		self.assertEqual(supplier_two.address, unicode('Kr 30 20 20'))
		self.assertNotEqual(supplier_one.address, supplier_two.address)
		self.assertEqual(supplier_one.phone, '1234567')
		self.assertEqual(supplier_two.phone, '123456798')
		self.assertNotEqual(supplier_one.phone, supplier_two.phone)