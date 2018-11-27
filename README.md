# primo.py
ejercicio1

 #!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

nprimos = []

def primo(numero):
    if numero<2:
        return False

    for i in range(2,numero):
       if numero%i == 0:
          return False
    return True



def  primos(numero,aumenta):
	if numero ==0:
		return nprimos
	else:
		if primo(aumenta):
			nprimos.append(aumenta)
			return primos(numero -1,aumenta +1)
		else:
			return  primos(numero,aumenta +1)



print primos(5,2)
