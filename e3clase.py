#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Juan Manual',
            'Ignacio',
            'Valeria',
            'Luis Antonio',
            'Pedro Alejandro',
            'Diana Guadalupe',
            'Jorge Luis',
            'Jesika',
            'Jesús Enrique',
            'Rafael Alejandro',
            'Servando Miguel',
            'Ricardo Omar',
            'Laura Patricia',
            'Isaías Abraham',
            'Oscar']

def alumnos():
    aprobados =[]
    reprobados = []
    for calif in  calificacion_alumno.values():
        if calif>=8:
           aprobados.append(calif)
        else: 
            reprobados.append(calif)
    return tuple(aprobados),tuple(reprobados)

def promedio():
    p=0
    cadena = "Calificaciones: "
    cal = []
    for prom in calificacion_alumno.values():
        p+=prom
        cal.append(prom)
    p/=len(becarios)
    for car in cal :
        cadena += str(car)
        cadena += ' '
    cadena += '\n'
    cadena += "Promedio: "
    cadena += str(p)
    return cadena


def conjunto():
    len({calificaciones})
    return conjunto


def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

asigna_calificaciones()
imprime_calificaciones()
print alumnos()
print promedio()