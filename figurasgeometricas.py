class FormaGeometrica:
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
class Triangulo(FormaGeometrica):
    base = None
    altura = None
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Quadrilatero(FormaGeometrica):
    base = None
    altura = None
    def calcular_area(self):
        return (self.base * self.altura)
        
class Circulo(FormaGeometrica):
    raio = None
    pi = 3.14
    def calcular_area(self):
        return (self.pi * (self.raio**2))
        
triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'Preto'
triangulo_a.cor_borda = 'Verde'
triangulo_a.espessura_borda = 3
triangulo_a.base = 100
triangulo_a.altura = 50
print(f'Triângulo de fundo: {triangulo_a.cor_fundo} e Área: {triangulo_a.calcular_area()} m².')

quadrado_a = Quadrilatero()
quadrado_a.cor_fundo = 'Amarelo'
quadrado_a.cor_borda = 'Preto'
quadrado_a.espessura_borda = 2
quadrado_a.base = 10
quadrado_a.altura = 10

print(f'Quadrado de fundo: {quadrado_a.cor_fundo} e Área: {quadrado_a.calcular_area()} m².')

circulo_a = Circulo()
circulo_a.cor_fundo = 'Azul'
circulo_a.cor_borda = 'Branca'
circulo_a.espessura_borda = 5
circulo_a.raio = 30

print(f'Circulo de fundo: {circulo_a.cor_fundo} e Área: {circulo_a.calcular_area()} m².')