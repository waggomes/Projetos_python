class Triangulo:
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isóceles'
        else:
            return 'escaleno'
    
    def retangulo(self):
        hipotenusa = max(self.a, self.b, self.c)
        
        if hipotenusa == self.a:
            cateto_1 = self.b
            cateto_2 = self.c
        elif hipotenusa == self.b:
            cateto_1 = self.a
            cateto_2 = self.c
        else:
            cateto_1 = self.a
            cateto_2 = self.b
        
        if hipotenusa ** 2 == cateto_1 ** 2 + cateto_2 ** 2:
            return True
        else:
            return False

    def semelhantes(self,triangulo):
        atual = [self.a, self.b, self.c]
        atual_ordenada = sorted(atual)
        novo = [triangulo.a, triangulo.b, triangulo.c]
        novo_ordenado = sorted(novo)

        if atual_ordenada == novo_ordenado:
            return True
        else:
            return False
    



