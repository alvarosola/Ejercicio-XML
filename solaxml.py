#!/usr/bin/python
#-*- coding: utf-8 -*--

#Ejercicio-XML

from lxml import etree
arbol= etree.parse("animal-en-adopcion.xml")

raiz=arbol.getroot()

#1 - Lista los animales que hay en adopción con su nombre y raza.

lista=raiz.findall("result/animal-en-adopcion/nombre")
lista1=raiz.findall("result/animal-en-adopcion/raza")

for x in lista:
	nombre=x.text

for i in lista1:
	raza=i.text
		
print "Nombre:",nombre,"y su raza es",raza


#2 - Muestra cuantos animales hay en adopción.

#3 - Pide por teclado años o meses, despues vuelve a pedir por teclado una edad mínima y edad máxima.

#4 - Pide por teclado una especie y que muestre todos los animales disponibles de esa especie.

#5 - Pide por teclado el tamaño de los animales y te diga de que especies hay disponibles de ese tamaño.