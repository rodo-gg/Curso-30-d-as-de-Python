# Variables 

my_first_variable = "Esto es una variable"
print(my_first_variable)

my_int_variable = 23
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Dentro de los prints podemos concatenar variables en un print, super facil como JS 
print(my_first_variable, my_int_variable,my_bool_variable)

#Esto es una prueba que alguna variable int la puedo convertir en str 
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
print("Esto es una variasble:",my_bool_variable)

#Algunas funciones del sistema 
print(len(my_first_variable))

name, surname, alias, age = "Rodolfo", "Vergara", "Mancora", 23

print("Mi nombre es:",name,"y mi apellido es:",surname, 'y mi edad es:',age) 

# Inputs
"""
first_name = input("¿Cual es tu nombre?: ")
age = input("y tu edad?")

print(first_name)
print(age)
"""
#Cambiamos su tipo 

name = 23
age = "Mancora"
print(name)
print(age)

#Forzar el tipado ? 
# Python es un lenguaje muy debil en ese sentido, cosa que no pasa con js 
addrees: str = "Mi dirección"
addrees = 23.5

print(addrees)
