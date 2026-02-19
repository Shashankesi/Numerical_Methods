import math

# Transcendental Function
def f(x):
    return x * math.exp(-x) - 0.1

# Derivative for Newton-Raphson
def df(x):
    return math.exp(-x) - x * math.exp(-x)


# ---------------- BISECTION METHOD ----------------
def bisection(a, b, tol):
    iterations = 0
    print("\nBisection Method Iterations:")
    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    
    while (b - a) >= tol:
        c = (a + b) / 2
        print(f"{iterations+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")
        
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iterations += 1
    
    return (a + b) / 2, iterations


# ---------------- REGULA FALSI METHOD ----------------
def regula_falsi(a, b, tol):
    iterations = 0
    print("\nRegula Falsi Method Iterations:")
    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{iterations+1}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}")
        
        if abs(f(c)) < tol:
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iterations += 1
    
    return c, iterations


# ---------------- NEWTON-RAPHSON METHOD ----------------
def newton_raphson(x0, tol):
    iterations = 0
    print("\nNewton-Raphson Method Iterations:")
    print("Iter\t x0\t\t x1\t\t f(x1)")
    
    while True:
        if df(x0) == 0:
            print("Derivative is zero. Method fails.")
            return None, iterations
        
        x1 = x0 - f(x0) / df(x0)
        print(f"{iterations+1}\t {x0:.6f}\t {x1:.6f}\t {f(x1):.6f}")
        
        if abs(f(x1)) < tol:
            break
        
        x0 = x1
        iterations += 1
    
    return x1, iterations


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    
    a = 0
    b = 1
    x0 = 0.5
    tolerance = 0.00001
    
    root_b, iter_b = bisection(a, b, tolerance)
    root_r, iter_r = regula_falsi(a, b, tolerance)
    root_n, iter_n = newton_raphson(x0, tolerance)
    
    print("\n\nFinal Results")
    print("-----------------------------------")
    print(f"Bisection Method   : Root = {root_b:.6f}, Iterations = {iter_b}")
    print(f"Regula Falsi Method: Root = {root_r:.6f}, Iterations = {iter_r}")
    print(f"Newton-Raphson     : Root = {root_n:.6f}, Iterations = {iter_n}")
    
    print("\nBest Method (Least Iterations):")
    
    min_iter = min(iter_b, iter_r, iter_n)
    
    if min_iter == iter_n:
        print("Newton-Raphson Method")
    elif min_iter == iter_r:
        print("Regula Falsi Method")
    else:
        print("Bisection Method")
