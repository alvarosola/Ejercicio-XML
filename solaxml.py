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

lista=raiz.xpath("//animal-en-adopcion")

for x in lista:
	print "Nombre:",x.find("nombre").text,"y su raza es",x.find("raza").text

#2 - Muestra cuantos animales y razas hay en total.

lista1=raiz.xpath("//animal-en-adopcion")

contador=0
for i in lista1:
	contador=contador+1
print "Hay un total de",contador,"animales con sus razas."
print "--------------------------------------------------"

#3 - Pide por teclado años o meses, despues vuelve a pedir por teclado una edad mínima y edad máxima.



#4 - Pide por teclado una especie y que muestre todos los animales disponibles de esa especie.

pregunta1=raw_input("Introduzca una especie:")

lista3=raiz.xpath("//animal-en-adopcion")
print "Los animales de esta especie que hay disponibles son:"

for especie in lista3:
	if especie.find("especie").text.lower()== pregunta1.lower():
		for nombre in especie.xpath("nombre"):
			print nombre.text

print "-----------------------------------------------------"
#5 - Pide por teclado el tamaño de los animales y te diga de que especies hay disponibles de ese tamaño.

pregunta2=raw_input("Introduzca una tamaño:")

lista4=raiz.xpath("//animal-en-adopcion")

for tamano in lista4:
	if pregunta2.title() in tamano.xpath("tamagno"):
		for tam in tamano.xpath("especie"):
			print tam.text