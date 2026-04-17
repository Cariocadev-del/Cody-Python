import math

co = float(input('digite um comprimento : '))
ca = float(input('digite o valor do cateto : '))


# A função hypot faz todo o trabalho de Pitágoras: raiz(co² + ca²)
hipotenusa = math.hypot(co, ca)

# Mostra o resultado final formatado com 2 casas decimais
print(f'O valor da hipotenusa é {hipotenusa:.2f}')
 