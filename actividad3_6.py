# 6.La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación.

# -Ingredientes vegetarianos: Pimiento y tofu.
# -Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
# de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
# puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
# ingredientes que lleva.

option = int(input('Ingresa el 1 si quieres una pizza vegetariana y el 2 si quieres una pizza con carne'))

if option == 1:
  optionVegetarianPizzas = int(input('Oprime 1 si deseas pimiento o 2 si dedeas tofu'))
  if optionVegetarianPizzas == 1:
    optionVegetarianPizzas = 'pimiento'
  elif optionVegetarianPizzas == 2:
    optionVegetarianPizzas = 'tofu'
  print('Tu elección es pizza vegetariana con: ', optionVegetarianPizzas)

elif option == 2:
  optionMeatPizzas =int(input('0prime 1 si deseas Peperoni o 2 si deseas Jamón ó 3 si deseas Salmón '))

  if optionMeatPizzas == 1:
    optionMeatPizzas = 'Peperoni'
  elif optionMeatPizzas == 2:
    optionMeatPizzas = 'Jamón'
  elif optionMeatPizzas == 2:
    optionMeatPizzas = 'Salmón'
  print('Tu elección es pizza de carne con: ', optionMeatPizzas)
