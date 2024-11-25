# 4. Para tributar un determinado impuesto se debe ser mayor de 18años y tener unos ingresos
# iguales o superiores a 3.000.000 mensuales. Escribir un programa que pregunte al usuario
# su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o
# no.

age = int(input('Ingresa tu edad: '))
monthSalary = int(input('Ingresa tus ingresos mensuales: '))

if age >= 18 and monthSalary >= 3000000:
  print('Tienes que tributar')
print('No tienes que tributar')
