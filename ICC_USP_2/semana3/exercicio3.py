"""
    Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.

t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5)
.tipo_lado()
# deve devolver 'escaleno'
"""
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if ((self.a == self.b ) and (self.b == self.c)):
            return "equilátero"
        elif ((self.a == self.b) or (self.a == self.c) or (self.b == self.c)):
            return "isóceles"
        else:
            return "escaleno"

# t = Triangulo(4, 4, 4)
# print(t.tipo_lado())
# # deve devolver 'equilátero'

# u = Triangulo(3, 4, 5)
# print(u.tipo_lado())
# # deve devolver 'escaleno'

# v = Triangulo(3,3,4)
# print(v.tipo_lado())
