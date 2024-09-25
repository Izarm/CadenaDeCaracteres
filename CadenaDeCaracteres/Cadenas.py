#1)
name = "Zhamuel"
age = 20
favouriteFood = "Pollo hawaiano"
Escribir = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}."
print(Escribir)

#2)
NombreCompleto = input("Por favor, ingresa tu nombre completo: ")
letter_count = len(NombreCompleto.replace(" ", ""))
Escribir2 = f"Hola, {NombreCompleto}! Tu nombre tiene {letter_count} letras, excluyendo los espacios."
print(Escribir2)

#3)
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078

RedondearIncrease = round(increaseSalesPercent,2)
Redondearrevenue = round(revenueGrowthPercent,2)

Escribir3 = f"Las ventas de la empresa láctea aumentaron un {RedondearIncrease:.2f}% y los ingresos crecieron un {Redondearrevenue:.2f}%. "
print(Escribir3)

#4)
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
Escribir4 = secretMessage[3::2]
print(Escribir4)

#5)
def contar_palabras(text):
  palabras = text.split()
  return len(palabras)
text = "El nombre \"Python\" viene dado por la afición de Van Rossum al grupo Monty Python."
Escribir5 = contar_palabras(text)
print(f"Número de palabras en la frase: {Escribir5}")

#6)
def reemplazarLetra(cadena, letraOriginal, letraNueva):
  return cadena.replace(letraOriginal, letraNueva)
word = "Camila"
Escribir6 = reemplazarLetra(word, "a", "e")
print(Escribir6)

#7)
def invertirPalabras(frase):
  palabras = frase.split()
  palabras.reverse()
  return " ".join(palabras)
Escribir7 = "La historia del lenguaje de programación Python"
PalabraInvertida = invertirPalabras(Escribir7)
print(PalabraInvertida)
