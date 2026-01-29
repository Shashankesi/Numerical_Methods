import math
def f(x):
    return x**2 - 4
def f_prime(x): 
    return 2*x 
def newton_raphson(x0, tol, max_iter=100):
    x=x0
    for i in range(1,1+max_iter):
        print(f"{i}\t {x:.6f}\t {f(x):.6f}")
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x
root=newton_raphson(1.0, 1e-8)
print(f"The root is approximately: {root:.6f}")
print(f"f(root) = {f(root):.6f}")