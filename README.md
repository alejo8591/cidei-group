## Aplicación de ejemplo para el Curso `Backend` y `Frontend`, construida en `Django`

### 1. Instalación de Software

#### 1.1. Instalación de Git

  Los sistemas operativos basados ​​en UNIX todos utilizan un terminal. También los descendientes, derivados y clones de UNIX incluyendo los de Apple (OS X) y las muchas distribuciones disponibles hoy en día disponibles para Linux. 
  Todos estos sistemas operativos contienen un conjunto básico de comandos que le ayudan a navegar a través de sus programas de sistemas de archivos y de lanzamiento, todo ello sin la necesidad de cualquier interfaz gráfica.
  Para sistemas operativos Windows; El proyecto `msysGit` tiene uno de los procesos de instalación más sencillos. Simplemente descargar el archivo `.exe` del instalador desde la página de GitHub, y ejecutar:

   * `http://msysgit.github.com/`

#### 1.2. Comandos básicos para tener en cuenta

  * **pwd**: imprime el directorio de trabajo actual a la terminal. Se muestra la ruta completa de dónde se encuentra actualmente. 

  * **ls**: Imprime una lista de archivos en el directorio de trabajo actual en la terminal.

  * **cd**: En combinación con una ruta, permite cambiar el directorio de trabajo actual. Por ejemplo, el comando `cd /home/username/` cambia el directorio de trabajo actual en `/home/username/`.

  * **cp**: copiar archivos y/o directorios. Debe proporcionar el origen y el destino. Por ejemplo, para hacer una copia de la models.py archivo en el mismo directorio, utilizar el comando `cp models.py models_backup.py`. 

  * **mv**: Mueve los archivos/directorios. Como cp, debe proporcionar el origen y el destino. Este comando también se utiliza para cambiar el nombre de los archivos.

  * **mkdir**: crea un directorio en su directorio de trabajo actual.

  * **rm**: Abreviatura de quitar, este comando elimina o borra los archivos del sistema de archivos. Debe proporcionar el nombre del archivo(s) que desea eliminar.

  * **rmdir**: Un comando alternativo para eliminar los directorios de su sistema de archivos. Proporcionar un directorio que desea eliminar. Una vez más, tenga cuidado: no se le solicitará que confirme sus intenciones. 

#### 1.3. Instalar el ambiente virtual para los Paquetes y/o Modulos en Python

##### 1.3.1. ¿Cómo instalar paquetes o modulos en Python?

  Dentro de los módulos que tiene por defecto python, y que vienen en la instalación, se encuentran `setuptools` y `easy_install` que en conjunto permiten descargar, construir, instalar y administrar paquetes de Python.

  > Para saber más acerca de `setuptools` y `easy_install` [visita la página en python.org](https://pypi.python.org/pypi/setuptools) y [la documentación oficial](http://pythonhosted.org//setuptools/)

  * Instalar `PyPi` con `setuptools` y `easy_install`: `easy_intall pip`

  ##### 1.3.2. Instalar `virtualenv` paquetes con PyPi

  Para instalar paquetes es necesario utilizar el comando `pip` en la linea de comandos:
  * `$ pip install virtualenv`

  ##### 1.3.3. Creando ambientes virtuales con `virtualenv`

  Para crear ambientes virtuales con `virtualenv` en Python
  * `$ virtualenv venv`

  ##### 1.3.4. activando ambiente virtual creado con `virtualenv`

  Para activar el ambiente virtual con `virtualenv` es necesario estar ubicado donde guardo el directorio `venv` y se activa de la siguiente manera
   * `source ven/bin/activate`
   * `(venv)$`

***

### 2. Iniciando con Django

#### 2.1. Instalación de Django

  Después de tener instalado Python, crear el ambiente virtual, llamado `venv`, y activarlo; se procede a instalar **Django**
   * `(venv)$ pip install django`
   * Probando la instalación de Django:

   ```python
    (venv)$ python -c "import django; print(django.get_version())"
    (venv)$ 1.6.5
   ```

#### 2.2. Creando un proyecto con **Django**
  
  Para crear un nuevo proyecto de **Django**, vaya a su directorio de código (es decir, el directorio `<workspace>`), y ejecute el siguiente comando:
   * `(venv)$ django-admin.py startproject sales`
