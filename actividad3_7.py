# 7. Los tramos impositivos para la declaración de la renta en un determinado país son los
# siguientes:


# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
# impositivo que le corresponde

rentaAnual = int(input('Ingrese su renta anual: '))

if rentaAnual <= 1000000:
  print(' le corresponde un tipo impositivo del 5%')

elif rentaAnual > 1000000 and rentaAnual < 2000000:
  print(' le corresponde un tipo impositivo del 15%')

elif rentaAnual > 2000000 and rentaAnual < 3500000:
  print(' le corresponde un tipo impositivo del 20%')

elif rentaAnual > 3500000 and rentaAnual < 6000000:
  print(' le corresponde un tipo impositivo del 30%')

elif rentaAnual > 6000000:
  print(' le corresponde un tipo impositivo del 45%')

