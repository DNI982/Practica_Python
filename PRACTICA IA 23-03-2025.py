# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 15:00:33 2025

@author: TNT
"""

# Ejercicio 1: 
precio_producto = 100
iva = 0.12
importe_iva = precio_producto * iva
precio_final = precio_producto + importe_iva

print(f"Importe del IVA: Q. {importe_iva}")
print(f"Precio final: Q. {precio_final}")

# Ejercicio 2: 
numero = 10
if 0 <= numero <= 10:
    print("El número está entre 0 y 10.")
else:
    print("El número no está entre 0 y 10.")
    
# Ejercicio 3:
numero1 = 21
if 0 <= numero1 <= 10:
    print("El número está entre 0 y 10.")
elif 11 <= numero1 <= 20:
    print("El número está entre 11 y 20.")
elif 21 <= numero1 <= 30:
    print("El número está entre 21 y 30.")
    
# Ejercicio 4: 
contador = 1
while contador <= 100:
    print(contador)
    contador += 1
    
# Ejercicio 5: 
for numero in range (1, 101):
    print(numero)
    
    
    
    
