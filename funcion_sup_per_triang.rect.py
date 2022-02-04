


def superficieTrianguloRectangulo(cateto1,cateto2):
  return (cateto1*cateto2)/2

def perimetroTriangulo(cateto1, cateto2):
   return (cateto1 + cateto2) + ((cateto1**2 + cateto2**2)**(0.5))


print("Perimetro de un triangulo rectangulo con Base=17cm y Altur=22cm es: ",perimetroTriangulo(17,22),"Cm")
print("Superficie de un triangulo rectangulo con Base=17cm y Altur=22cm es: ",superficieTrianguloRectangulo(17,22),"Cm2")
print("Perimetro de un triangulo rectangulo con Base=2cm y Altur=4cm es: ",perimetroTriangulo(2,4),"Cm")
print("Superficie de un triangulo rectangulo con Base=2cm y Altur=4cm es: ",superficieTrianguloRectangulo(2,4),"Cm2")

