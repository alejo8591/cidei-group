## Aplicación de ejemplo para el Curso `Backend` y `Frontend`, construida en `Django`

### 1. Instalación de Software

#### 1.1. Instalación de Git

: Los sistemas operativos basados ​​en UNIX todos utilizan un terminal. También los descendientes, derivados y clones de UNIX incluyendo los de Apple (OS X) y las muchas distribuciones disponibles hoy en día disponibles para Linux. 
: Todos estos sistemas operativos contienen un conjunto básico de comandos que le ayudan a navegar a través de sus programas de sistemas de archivos y de lanzamiento, todo ello sin la necesidad de cualquier interfaz gráfica.
: Para sistemas operativos Windows; El proyecto `msysGit` tiene uno de los procesos de instalación más sencillos. Simplemente descargar el archivo `.exe` del instalador desde la página de GitHub, y ejecutar:

:  * `http://msysgit.github.com/`

#### 1.2. Comandos básicos para tener en cuenta

: * **pwd**: imprime el directorio de trabajo actual a la terminal. Se muestra la ruta completa de dónde se encuentra actualmente. 

: * **ls**: Imprime una lista de archivos en el directorio de trabajo actual en la terminal.

: * **cd**: En combinación con una ruta, permite cambiar el directorio de trabajo actual. Por ejemplo, el comando `cd /home/username/` cambia el directorio de trabajo actual en `/home/username/`.

: * **cp**: copiar archivos y/o directorios. Debe proporcionar el origen y el destino. Por ejemplo, para hacer una copia de la models.py archivo en el mismo directorio, utilizar el comando `cp models.py models_backup.py`. 

: * **mv**: Mueve los archivos/directorios. Como cp, debe proporcionar el origen y el destino. Este comando también se utiliza para cambiar el nombre de los archivos.

: * **mkdir**: crea un directorio en su directorio de trabajo actual.

: * **rm**: Abreviatura de quitar, este comando elimina o borra los archivos del sistema de archivos. Debe proporcionar el nombre del archivo(s) que desea eliminar.

: * **rmdir**: Un comando alternativo para eliminar los directorios de su sistema de archivos. Proporcionar un directorio que desea eliminar. Una vez más, tenga cuidado: no se le solicitará que confirme sus intenciones. 

#### 1.3. Instalar el ambiente virtual para los Paquetes y/o Modulos en Python

: ##### 1.3.1. ¿Cómo instalar paquetes o modulos en Python?

:    Dentro de los módulos que tiene por defecto python, y que vienen en la instalación, se encuentran `setuptools` y `easy_install` que en conjunto permiten descargar, construir, instalar y administrar paquetes de Python.

:  > Para saber más acerca de `setuptools` y `easy_install` [visita la página en python.org](https://pypi.python.org/pypi/setuptools) y [la documentación oficial](http://pythonhosted.org//setuptools/)

:    * Instalar `PyPi` con `setuptools` y `easy_install`: `easy_intall pip`

: ##### 1.3.2. Instalar `virtualenv` paquetes con PyPi

:  Para instalar paquetes es necesario utilizar el comando `pip` en la linea de comandos:
:  * `$ pip install virtualenv`

: ##### 1.3.3. Creando ambientes virtuales con `virtualenv`

:  Para crear ambientes virtuales con `virtualenv` en Python
:  * `$ virtualenv venv`

: ##### 1.3.4. activando ambiente virtual creado con `virtualenv`

:  Para activar el ambiente virtual con `virtualenv` es necesario estar ubicado donde guardo el directorio `venv` y se activa de la siguiente manera
:  * `source ven/bin/activate`
:  * `(venv)$`

***

### 2. Iniciando con Django

#### 2.1. Instalación de Django

:  Después de tener instalado Python, crear el ambiente virtual, llamado `venv`, y activarlo; se procede a instalar **Django**
:  * `(venv)$ pip install django`
:  * Probando la instalación de Django:
```python
(venv)$ python -c "import django; print(django.get_version())"
(venv)$ 1.6.5
```

#### 2.2. Creando un proyecto con Django

:  Para crear un nuevo proyecto de **Django**, vaya a su directorio de código (es decir, el directorio `<workspace>`), y ejecute el siguiente comando:
:  * `(venv)$ django-admin.py startproject food_store`
:  Para probar el proyecto utilizar el `manage.py`, ejecutar el siguiente comando:
:  * `(venv)$ python manage.py runserver`


#### 2.3. Creando una aplicación dentro de un proyecto Django

:  Un proyecto de Django es una colección de configuraciones y aplicaciones que componen una aplicación web determinada o página web:
:  * `(venv)$ django-admin.py startapp sales`
:  Para probar el proyecto de nuevo se sigue utilizando el script `manage.py`:
:  * `(venv)$ python manage.py runserver`
La aplicación no debe arrojar errores pues no ha sido instalada.

##### 2.3.1. Instalando aplicación al proyecto

El comando `startapp` crea un nuevo directorio en la raíz del proyecto. Como era de esperar, este directorio se llama `sales`:

```
sales/
	|-- __init__.py
	|-- admin.py
	|-- models.py
	|-- tests.py
	`-- views.py
```
Las aplicaciones se deben "instalar" en el script `settings.py` en la tupla `INSTALLED_APPS` de la siguiente manera:
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sales',
)
```

##### 2.3.2. Trabajando con el Modelo de `sales`

:  Con base en la información creamos los diferentes modelos para la aplicación `sales`:
     : * **Categories**: los detalles de la categoria para los productos
     : * **Suppliers**: Referente a los proveedores de los productos
     : * **Products**: Los productos que vende la tienda
     : * **Orders**: Las ordenes que se generan cuando se compra
     : * **OrderDetail**: Detalles de la orden de compra

:  El siguiente es el `models.py` de la aplicación `sales`

```python
# -*- coding:utf-8 -*-
# models.py
from django.db import models

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
	supplier = mdoels.ForeignKey(Suppliers)
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
```