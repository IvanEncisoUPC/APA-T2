"""
Módulo con funciones para el manejo de números primos.

Autores: Ivan Enciso & Pau Codina

Fecha: 2023-11-15
"""

def es_primo(numero):
  """
  Comprueba si un número es primo.

  Parámetros:
    numero: El número a comprobar.

  Salida:
    True si el número es primo, False en caso contrario.
  """
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

def generar_primos(n):
  """
  Genera una lista con los números primos hasta un límite dado.

  Parámetros:
    n: El límite superior para la generación de números primos.

  Salida:
    Una lista con los números primos hasta n.
  """
  primos = [2]
  for i in range(3, n + 1, 2):
    if es_primo(i):
      primos.append(i)
  return primos

def main():
  """
  Función principal para probar las funciones del módulo.
  """
  numero = 11
  print(f"El número {numero} {'es' if es_primo(numero) else 'no es'} primo")

  n = 20
  primos = generar_primos(n)
  print(f"Los primeros {n} números primos son: {primos}")

if __name__ == "__main__":
  main()