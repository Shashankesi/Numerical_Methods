import math

def f(x, y):
    return x + y


def rk4(x0, y0, h, n):

    print("\n--- Runge-Kutta Method (4th Order) ---")
    print(f"Initial Value : x0 = {x0}, y0 = {y0}")
    print(f"Step size (h) : {h}")
    print(f"Number of steps : {n}")

    print("\n-------------------------------------------------------------------")
    print("Step    x        y        k1        k2        k3        k4        y_next")
    print("-------------------------------------------------------------------")

    x = x0
    y = y0

    for i in range(1, n + 1):

        k1 = f(x, y)
        k2 = f(x + h/2, y + (h/2)*k1)
        k3 = f(x + h/2, y + (h/2)*k2)
        k4 = f(x + h, y + h*k3)

        y_next = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

        print(f"{i:<7}{x:<9.4f}{y:<9.4f}{k1:<10.4f}{k2:<10.4f}{k3:<10.4f}{k4:<10.4f}{y_next:.6f}")

        x = x + h
        y = y_next

    print("-------------------------------------------------------------------")
    print(f"Final Result : y({x:.2f}) = {y:.6f}")
    print("-------------------------------------------------------------------\n")

    return y


x0 = 0
y0 = 1
h = 0.1
n = 10

rk4(x0, y0, h, n)