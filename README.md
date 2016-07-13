# Debianizado

Debianizar consiste en agregar en el directorio raíz de nuestro código fuente, una carpeta 'debian' con los archivos necesarios (configuración, scripts de instalación, etc) tal como se indica en la Política de Debian[1] y en los Manuales para desarrolladores de Debian[2].

Existen herramientas para debianizar proyectos de forma semiautomatica como dh_make[3], sin embargo esta herramienta tiene ciertas limitaciones -no genera automáticamente el archivo de control ni verifica las dependencias del paquete- y requiere trabajo adicional; genera mas contenido de lo estrictamente necesario, lo cual puede generar confusión para quien se este iniciando en el proceso de debianización de código fuente. Por esta razón se describe a continuación el contenido mínimo necesario (genérico) que debe tener un paquete fuente debianizado.

## CHANGELOG

### Ubicación

`debian/changelog`

Descripción: En este archivo se lleva un breve registro explicando las modificaciones y/o mejoras realizadas al código fuente. Se recomienda no generar este archivo a mano, dado que utiliza un formato especial y son frecuentes los errores cuando se genera manualmente. En su lugar se recomienda usar la herramienta dch[4] para generarlo automáticamente. Para mas detalles consulte el apartado 4.4 en https://www.debian.org/doc/debian-policy/ch-source.html y el 4.3 en https://www.debian.org/doc/manuals/maint-guide/dreq.es.html#changelog

### Formato

```
paquete (version) distribucion(es); prioridad=prioridad
    [linea vacia, opcional]
  * explicacion de las modificaciones
    mas detalles acerca de las modificaciones
	[linea vacia]
  * otros cambios 
	[linea vacia, opcional]
-- nombre del mantenedor <correo del mantenedor>[dos espacios]  fecha

```
### Ejemplos

```
canaima-servicios (0.1.6) stable; urgency=medium

  * [a5457a4] Actualizando dependencias de construcción

 -- Victor Pino <victopin0@gmail.com>  Wed, 20 Jan 2016 11:22:37 -0430
```

```
canaima-servicios (0.1.3) stable; urgency=medium

  [ Francisco Guerrero ]
  * [be35e85] Ajustando recursos de paquetes y pinning

  [ Victor Pino ]
  * [71212d3] Actualizando CRUD de pinnings y paginador

 -- Victor Pino <victopin0@gmail.com>  Wed, 13 Jan 2016 10:51:53 -0430
```

```
canaima-servicios (0.1.2) stable; urgency=medium

  [ Francisco Guerrero ]
  * [546c532] Configurando setup.py
  * [f52e30e] Corrigiendo configuracion de uwsgi y otros errores menores
  * [63070a2] Actualizando modelo de repositorios
  * [247b354] Actualizando gitignore
  * [42ba0ba] Corrigiendo generacion del basename de repositorios

  [ Victor Pino ]
  * [8d32589] Añadiendo nuevo modulos y funciones

 -- Victor Pino <victopin0@gmail.com>  Tue, 12 Jan 2016 17:11:17 -0430
```

## RULES

### Ubicación

`debian/rules`

### Descripción

Es un script con sintaxis de Makefile, debe tener permisos de ejecución. Contiene instrucciones especificas para generar los paquetes binarios a partir de las fuentes, utilizando un conjunto de ayudantes[8] que automatizan tareas repetitivas del proceso de empaquetamiento. Para mas detalles consulte el apartado 4.9 en https://www.debian.org/doc/debian-policy/ch-source.html

### Ejemplo

```
#!/usr/bin/make -f

%:
    dh $@
```

## COMPAT

### Ubicación

`debian/compat`


### Descripción 

El archivo compat define el nivel de compatibilidad de debhelper. Actualmente, se establece la compatibilidad a la versión 9 de debhelper como se indica a continuación.

### Ejemplo

```
9
```

## CONTROL

### Ubicación 

`debian/control`

### Descripción

Archivo de texto que contiene información sobre el paquete. Contiene varios valores que dpkg, dselect, apt-get, apt-cache, aptitude y otras herramientas de gestión de paquetes usarán para gestionar el paquete. Esta divido en dos secciones, una para la información sobre el paquete fuente y otra para el/los paquetes binarios. Su contenido está desglosado en https://www.debian.org/doc/debian-policy/ch-controlfields.html

### Ejemplo

```
Source: sedi
Section: web
Priority: standard
Maintainer: Centro Nacional de Tecnologías de la Información <responsable@cnti.gob.ve>
Build-Depends: debhelper (>= 9)
Standards-Version: 3.9.6
Homepage: http://canaima.softwarelibre.gob.ve/

Package: sedi
Architecture: all
Depends: bash, openjdk-7-jre, openjdk-7-jdk, mysql-server, apache2, logrotate, sed, python
Priority: optional
Description: Paquete de instalación semiautomático para sedi.
```

## INSTALL

### Ubicación

`debian/install`

### Descripción

Si hay archivos que deben ser instalados por el paquete pero no lo hace make install, puedes listar los archivos y/o directorios seguido del los respectivos destinos en el archivo install. Para mas detalles consulte https://www.debian.org/doc/manuals/maint-guide/dother.es.html#install

### Formato

```
src/archivo_binario usr/bin
src/archivo_configuracion etc/
```

[1] https://www.debian.org/doc/debian-policy/

[2] https://www.debian.org/doc/devel-manuals.es.html#policy

[3] http://manpages.ubuntu.com/manpages/karmic/man8/dh_make.8.html

[4] http://manpages.ubuntu.com/manpages/precise/en/man1/dch.1.html

[5] https://www.debian.org/doc/manuals/maint-guide/index.en.html

[6] https://www.debian.org/doc/debian-policy/ch-source.html

[7] https://www.debian.org/doc/debian-policy/ch-binary.html

[8] http://manpages.ubuntu.com/manpages/hardy/es/man7/debhelper.7.html