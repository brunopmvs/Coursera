"""
Exercício 1: Triângulos retângulos
Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.

Exemplos:
t = Triangulo(1, 3, 5)
t.retangulo()
# deve devolver False

u = Triangulo(3, 4, 5)
u.retangulo()
# deve devolver True
"""

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        hipotenusa = self.a
        catetoA = self.b
        catetoB = self.c

        if ((self.b > self.a) and (self.b > self.c)):
            hipotenusa = self.b
            catetoA = self.a
            catetoB = self.c
        if ((self.c > self.a) and (self.c > self.a)):
            hipotenusa = self.c
            catetoA = self.b
            catetoB = self.a
        
        if ( (pow(hipotenusa, 2) == ( (pow(catetoA,2) + pow(catetoB,2) ) ) ) ):
            return True
        else:
            return False
t = Triangulo(1, 3, 5)
print(t.retangulo())
# deve devolver False

u = Triangulo(3, 4, 5)
print(u.retangulo())
# deve devolver True