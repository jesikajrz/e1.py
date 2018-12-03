#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import sys
import csv
import xml.etree.ElementTree as ET
import hashlib 
from datetime import datetime


hostsup =[]
md5_file= " "
m5=hashlib.md5()
sha1_file= " "
sh1=hashlib.sha1()
resultado= " "

class report():
	def __init__(self, hostdown,hostup,hostPorts,Domain,honey,address):
		self.hostdown = prendido
		self.hostup = apagado
		self.hostPorts = puertos
		self.Domain = Dominio
		self.honey  = honey
		self.address= address

	def __srt__(self):
		return '%s:%s:%s:%s:%s:\n' % (self.hostdown,
									  self.hostup,
									  self.hostPorts,
									  self.Domain,
									  self.honey,
									  self.address)
def readXml(archivo_nmap):
	with open ('archivo_nmap','r') as nmap:
		   algoritmo = nmap.read()
		   m5.update(algoritmo)
		   sh1.update(algoritmo)
		   return ET.fromstring(algoritmo)

def ports():
	for report in root.findall('ports'):
		hostdown=0
		hostup=0
		hostPorts=0
		Domain=0
		honey= " "
		address=" "
		if ports.find("status").get("state")=="up":
		
		else:
		   down ==0	





def este_es_el_reporte(archivo_reporte,resultado):
	print resultado
	with open (archivo_reporte,"w")as output:
		output.write(resultado)



def este_es_el_reporte_csv():
	with open("archivo_reporte.csv","w")as reporte:
		output=csv.writer(reporte)
		output.writerow(str(datetime.now()) + "\n","hostup","hostdown","Domain","honey","address")
		map(lambda r:output.write(str(r)),root)



if __name__=='__name__':
	lee_xml(sys.argv[1])
	escribe_reporte(sys.argv[2])






