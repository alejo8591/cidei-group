from django.db import models
# http://i.msdn.microsoft.com/dynimg/IC141637.gif

class Categories(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	picture = models.ImageField(upload_to="images")
	posted_on = models.DateTimeField(auto_now_add=True)

class Suppliers(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	address = models.CharField(max_length=255)
	phone = models.CharField(max_length=12)
	posted_on = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
	name = models.CharField(max_length=255)
	value = models.PositiveIntegerField()
	category = models.ForeignKey(Categories)
	supplier = models.ForeignKey(Suppliers)
	unit_price = models.PositiveIntegerField()
	units_in_stock = models.PositiveIntegerField()
	discontinued = models.BooleanField(default=True)
	posted_on = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
	description = models.TextField(null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)

class OrderDetail(models.Model):
	order = models.ForeignKey(Orders)
	quantity = models.PositiveIntegerField()
	discount = models.PositiveIntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)