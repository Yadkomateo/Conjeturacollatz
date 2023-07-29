# Conjeturacollatz
El programa solicita al usuario que ingrese un valor numérico mediante la función input. El valor ingresado se guarda en la variable number como un entero usando int().

A continuación, el código verifica si el número ingresado es menor o igual a cero con el condicional if number <= 0:. Si el número no es positivo (es cero o negativo), el programa genera una excepción (error) usando raise ValueError("El número debe ser mayor que cero."). Esto asegura que el número ingresado sea un valor positivo, ya que la secuencia de Collatz solo está definida para números enteros positivos.

Se inicializa una lista llamada secuencia que contendrá los valores de la secuencia de Collatz para el número ingresado. El primer valor de esta lista es el número ingresado inicialmente.

Luego, se inicia un bucle while number != 1: que continuará hasta que el valor de number sea igual a 1, que es el valor al que se supone que la secuencia de Collatz siempre converge.

Dentro del bucle, se verifica si el número actual (number) es par o impar usando if number % 2 == 0:. El operador % calcula el residuo de la división por 2, y si el resultado es 0, el número es par.

Si el número es par, se divide entre 2 usando number = number // 2. Si es impar, se multiplica por 3 y se le suma 1 usando number = 3 * number + 1.

Después de cada iteración del bucle, el valor actual de number se agrega a la lista secuencia usando secuencia.append(number).

El bucle continúa hasta que el valor de number es igual a 1. En ese momento, la secuencia de Collatz ha llegado a su final, y la lista secuencia contiene todos los valores de la secuencia desde el número inicial hasta 1.

Finalmente, el programa imprime la lista secuencia completa, mostrando la secuencia de Collatz generada para el número ingresado.
Conjetura Collatz en python resuelto 
