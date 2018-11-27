#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import random
def genera(psswd):
	digitos = str(random.randint(0,9))
	minusculas = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w",",X","y","z"])
	mayusculas = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
	caracteres = random.choice(["!","#","$","%","&","/","(",")","?","¡","+","-",])
	eleccion = random.choice(["minusculas","mayusculas","caracteres","digitos"])
	if eleccion =="minusculas": 
		seguro = minusculas
	elif eleccion =="mayusculas":
		seguro = mayusculas
	elif eleccion =="caracteres":
		 seguro =caracteres
	elif eleccion =="digitos":
		seguro=digitos
	if (len(psswd)<=7):
		return genera(psswd + seguro)
	else:
		return psswd


print genera("")
