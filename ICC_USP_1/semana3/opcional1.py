"""
Exercício 1 - Distância entre dois pontos
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
longe
na saída. Caso o contrário, quando a distância for menor que 10, imprima
perto
Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:
d(x,y)=(x1−x2)2+(y1−y2)2 d(x, y) = \sqrt{(x_1 - x_2) ^2 + (y_1 - y_2)^2} d(x,y)=(x1​−x2​)2+(y1​−y2​)2

"""
import math

x1 = int(input("Informe o valor X do primeiro ponto:"))
y1 = int(input("Informe o valor Y do primeiro ponto:"))
x2 = int(input("Informe o valor X do segundo ponto:"))
y2 = int(input("Informe o valor Y do segundo ponto:"))

distance = math.sqrt((pow(x1-x2,2))+pow(y1-y2, 2))

if(distance < 10):
    print("perto")
else:
    print("longe")

print(distance)