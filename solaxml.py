#!/usr/bin/python
#-*- coding: utf-8 -*--

#Ejercicio-XML

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from lxml import etree
arbol= etree.parse("animal-en-adopcion.xml")

raiz=arbol.getroot()

#1 - Lista los animales que hay en adopción con su nombre y raza.

lista=raiz.xpath("//resultado/result/animal-en-adopcion")

for x in lista:
	print "Nombre:",x.xpath("nombre/text()")[0],"y su raza es",x.xpath("raza/text()")[0]

#2 - Muestra cuantos animales hay en adopción.

#3 - Pide por teclado años o meses, despues vuelve a pedir por teclado una edad mínima y edad máxima.

#4 - Pide por teclado una especie y que muestre todos los animales disponibles de esa especie.

#5 - Pide por teclado el tamaño de los animales y te diga de que especies hay disponibles de ese tamaño.