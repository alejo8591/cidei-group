# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext
from sales.models import Categories, Suppliers, Products, Orders, OrderDetail
from sales.forms import Categories, SuppliersForm, ProducsForm, OrdersForm, OrderDetailForm
# Modulo serializador de QuerySets para Django
from django.http import HttpResponse
from django.core.serializers import serialize
import json

from django.contrib.auth.decorators import login_required

def index(request):
	context = Context({'title' : 'Hola CIDEI'})
	return render_to_response('app/index.html', context, context_instance=RequestContext(request))

@login_required()
def categories(request):
	categories = Category.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'categories' : categories})
	return render_to_response('app/categories.html', context)

@login_required()
def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	context = Context({'title' : 'Detalle categoria', 'category' : category})
	return render_to_response('app/category-details.html', context)

@login_required()
def add_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			# Crear un nuevo category
			category = Category.objects.create(
				name = form.cleaned_data['name'],
				slug = form.cleaned_data['slug'],
				description = form.cleaned_data['description'],
				update_category = form.cleaned_data['update_category']
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/app/categories/%s/' % category.slug)
	else:
		form = CategoryForm()

	context = Context({'title':'Creación de categorias', 'form': form})
	return render_to_response('app/add-category.html', context, context_instance=RequestContext(request))

@login_required()
def edit_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category.name = form.cleaned_data['name']
			category.slug = form.cleaned_data['slug'] 
			category.save()

			return HttpResponseRedirect('/app/categories/%s/' % category.slug)
	else:
		category_data = {
			'name' : category.name,
			'slug' : category.slug
		}

		form = CategoryForm(initial=category_data)

	context = Context({'title' : 'Editar la Categoria', 'form' : form, 'info_button' : 'Actualizar Categoria'})
	return render_to_response('app/add-category.html', context, context_instance=RequestContext(request))

@login_required()
def items(request):
	items = Item.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'items' : items})
	return render_to_response('app/items.html', context)

@login_required()
def item(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	pictures = Picture.objects.filter(item=item)
	count_pictures = pictures.count()
	context = Context({
		'title' : 'Hola CIDEI',
		'item' : item,
		'pictures':pictures,
		'count_pictures' : count_pictures
	})
	return render_to_response('app/item-details.html', context)

@login_required()
def add_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			# Crear un nuevo item
			item = Item.objects.create(
				listing = form.cleaned_data['listing'],
				name = form.cleaned_data['name'],
				category=form.cleaned_data['category'],
				department=form.cleaned_data['department'],
				description = form.cleaned_data['description'],
				update_item = form.cleaned_data['update_item'],
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/app/items/%s/' % item.id)
	else:
		form = ItemForm()

	context = Context({'title' : 'Adicionar item', 'form' : form})
	return render_to_response('app/add-item.html', context, context_instance=RequestContext(request))

@login_required()
def items(request):
	items = Item.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'items' : items})
	return render_to_response('app/items.html', context)

@login_required()
def item(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	pictures = Picture.objects.filter(item=item)
	count_pictures = pictures.count()
	context = Context({
		'title' : 'Hola CIDEI',
		'item' : item,
		'pictures':pictures,
		'count_pictures' : count_pictures
	})
	return render_to_response('app/item-details.html', context)

@login_required()
def add_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			# Crear un nuevo item
			item = Item.objects.create(
				listing = form.cleaned_data['listing'],
				name = form.cleaned_data['name'],
				category=form.cleaned_data['category'],
				department=form.cleaned_data['department'],
				description = form.cleaned_data['description'],
				update_item = form.cleaned_data['update_item'],
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/app/items/%s/' % item.id)
	else:
		form = ItemForm()

	context = Context({'title' : 'Adicionar item', 'form' : form})
	return render_to_response('app/add-item.html', context, context_instance=RequestContext(request))

def ajax_items(request):
	if request.is_ajax():
		items = Item.objects.all()
		print items
		items = serialize('json', items)
		print items
		items = json.dumps(items)
		print items

		return HttpResponse(items, content_type='application/json')
	else:
		return HttpResponse({'error' : 'Hubo un error'}, content_type='application/json')

