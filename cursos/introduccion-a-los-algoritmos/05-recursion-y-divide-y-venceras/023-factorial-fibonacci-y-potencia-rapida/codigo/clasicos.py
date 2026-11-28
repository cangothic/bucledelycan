# ep. 023 · Factorial, Fibonacci y potencia rápida
# Tres recursiones clásicas: una vuela y otra se arrastra.
import timeit


def factorial(n):
    if n == 0:
        return 1  # caso base: 0! = 1
    return n * factorial(n - 1)


llamadas = 0  # cuántas veces se llama a fib


def fib(n):
    global llamadas
    llamadas += 1
    if n < 2:
        return n  # fib(0) = 0, fib(1) = 1
    return fib(n - 1) + fib(n - 2)


def fib_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # los dos últimos, un paso más
    return a


def potencia_rapida(x, n):
    if n == 0:
        return 1  # caso base: x^0 = 1
    mitad = potencia_rapida(x, n // 2)  # una sola vez
    resultado = mitad * mitad
    if n % 2 == 1:
        resultado = resultado * x  # n impar: una x aparte
    return resultado


if __name__ == "__main__":
    print("5! =", factorial(5))

    llamadas = 0
    print("fib(30) =", fib(30))
    print("llamadas:", llamadas)
    tiempos = timeit.repeat(lambda: fib(30),
                            number=1, repeat=3)
    print(f"tiempo: {min(tiempos):.2f} s")

    print("fib_iterativo(100) =", fib_iterativo(100))
    print(potencia_rapida(2, 1000) == 2 ** 1000)
