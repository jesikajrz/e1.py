#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import re 
import sys 



def dirIP():
	with open ('direcciones.txt', 'r')as input_file:
	     for line in input_file.readlines():
			patron = r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{1,3}"
			if re.search(patron , "r"):
				return ips.append()
 


