# 5.Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
# programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si
# el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $
# 5.000 y si es mayor de 18 años, $ 10.000.

age = int(input('Ingresa tu edad: '))

if age < 4:
  print('Puedes entrar gratis')

if age >= 4 and age <= 18:
  print('Debes pagar $5 000')

if age > 18:
  print('Debes pagar $10 000')