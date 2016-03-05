#!/usr/bin/python
#-*- coding: utf-8 -*-

#Ejercicio-XML

from lxml import etree
arbol= etree.parse("animal-en-adopcion.xml")

raiz=arbol.getroot()

#1 - Lista los animales que hay en adopción con su nombre y raza.

lista=raiz.xpath("//animal-en-adopcion")

print "Lista de animales en adopción:"

for x in lista:
	print "Nombre:",x.find("nombre").text,"y su raza es",x.find("raza").text

#2 - Muestra cuantos animales y razas hay en total.

lista1=raiz.xpath("//animal-en-adopcion")

print "--------------------------------------------------"
contador=0
for i in lista1:
	contador=contador+1
print "Hay un total de",contador,"animales con sus razas."
print "--------------------------------------------------"

#3- Pide por teclado una edad, cachorro(0-3 meses), joven (3-12 meses), adulto(1-5 años), o mayor(>5 años) y despues devuelve los animales que hay disponibles de esa edad.

lista2=raiz.xpath("//animal-en-adopcion")

pregunta=raw_input("Introduzca una edad (cachorro(0-3 meses), joven (3-12 meses), adulto(1-5 años) o mayor(>5años):")

if pregunta=="cachorro" or "joven" or "adulto" or "mayor":
	for edad in lista2:
		if pregunta.title() in edad.findtext("edad"):
			for animal in edad.xpath("nombre"):
				print animal.text

print "-----------------------------------------------------"

#4 - Pide por teclado una especie y que muestre todos los animales disponibles de esa especie.

lista3=raiz.xpath("//animal-en-adopcion")

pregunta1=raw_input("Introduzca una especie (canina, felina, otros):")

print "Los animales de esta especie que hay disponibles son:"

for especie in lista3:
	if especie.find("especie").text.lower()== pregunta1.lower():
		for nombre in especie.xpath("nombre"):
			print nombre.text

print "-----------------------------------------------------"

#5 - Pide por teclado el tamaño de los animales y te diga de que especies hay disponibles de ese tamaño.

lista4=raiz.xpath("//animal-en-adopcion")

pregunta2=unicode(raw_input("Introduzca una tamaño:"),'utf8')
contador1=0

for tamagno in lista4:
	#contador1+=1
	contador1=1
	if pregunta2.title() in tamagno.findtext("tamagno"):
		for tam in tamagno.xpath("especie"):
			print "Hay",contador1,"de la especie",tam.text
