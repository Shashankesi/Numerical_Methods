import math

def f(x):
    return 1 / (1 + x**(5/2))


def simpsons_one_third(a, b):
    n = 10
    if n % 2 != 0:
        n += 1

    h = (b - a) / n

    print("\n--- Simpson's 1/3 Rule ---")
    print(f"Interval      : [{a}, {b}]")
    print(f"Subintervals  : {n}")
    print(f"Step size (h) : {h:.4f}")

    x = []
    fx = []

    print("\n------------------------------------")
    print("Index      x            f(x)")
    print("------------------------------------")

    for i in range(n + 1):
        xi = a + i * h
        fxi = f(xi)
        x.append(xi)
        fx.append(fxi)
        print(f"{i:<10}{xi:<12.4f}{fxi:.6f}")

    odd_sum = sum(fx[i] for i in range(1, n, 2))
    even_sum = sum(fx[i] for i in range(2, n, 2))

    print("\n------------------------------------")
    print(f"Sum of odd terms  = {odd_sum:.6f}")
    print(f"Sum of even terms = {even_sum:.6f}")

    result = (h / 3) * (fx[0] + fx[n] + 4 * odd_sum + 2 * even_sum)

    print("\n------------------------------------")
    print("Final Calculation:")
    print("I = (h/3)[f(x0) + f(xn) + 4(odd) + 2(even)]")
    print(f"I = ({h:.4f}/3)[{fx[0]:.6f} + {fx[n]:.6f} + 4({odd_sum:.6f}) + 2({even_sum:.6f})]")
    print("------------------------------------")
    print(f"Final Result = {result:.6f}")
    print("------------------------------------\n")

    return result


a = 0
b = 1

simpsons_one_third(a, b)