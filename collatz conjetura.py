"Collatz"
number = int(input("Ingrese un valor numérico: "))
if number <= 0:
    raise ValueError("El número debe ser mayor que cero.")

secuencia = [number]

while number != 1:
    if number % 2 == 0:
        number = number // 2 
    else:
        number = 3 * number + 1
    secuencia.append(number)

print("Secuencia de Collatz:", secuencia)

'''
 The Collatz conjecture, also known as the 3n+1 conjecture or the Collatz problem, is a famous unsolved problem in mathematics. The conjecture is named 
after German mathematician Lothar Collatz, who first proposed it in 1937.
La conjetura sugiere que sin importar cuál sea el número entero positivo con el que empecemos, este proceso iterativo eventualmente llegará al valor 1, y luego continuará en un ciclo 
infinito: 1 → 4 → 2 → 1 → 4 → 2 → 1 → y así sucesivamente.
'''