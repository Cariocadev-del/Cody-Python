#Crie um programa que lei quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar

carteira = float(input("Quantos reais vc tem na cateira?: "))

if carteira <= 3.27:
  print("Você não tem dinheiro o suficiente pra comprar Dolar")
else:
  print(f"Que legal!! Com isso você pode comprar {carteira/3.27} Dolares!!")
#  if exemplo == 2:
#  print("Valor é 2!!")
# elif exemplo >= 15:
#   print("Valor é maior ou igual a 15!!")
# else:
#   print("O valor não é 2 e nem maior ou igual a 15!!")

