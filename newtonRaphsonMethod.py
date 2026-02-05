# import math
# def f(x):
#     return x**2 - 4
# def f_prime(x): 
#     return 2*x 
# def newton_raphson(x0, tol, max_iter=100):
#     x=x0
#     for i in range(1,1+max_iter):
#         print(f"{i}\t {x:.6f}\t {f(x):.6f}")
#         x_new = x - f(x) / f_prime(x)
#         if abs(x_new - x) < tol:
#             return x_new
#         x = x_new
#     return x
# root=newton_raphson(1.0, 1e-8)
# print(f"The root is approximately: {root:.6f}")
# print(f"f(root) = {f(root):.6f}")


# polynomial function and its derivative
# def f(x):
#     return x**3 - x - 2

# def df(x):
#     return 3*x**2 - 1

# def newton_raphson(x0, tol, max_iter=20):
#     print("Iter     Current x        f(x)              Error")
#     print("---------------------------------------------------------")

#     for i in range(1, max_iter + 1):
#         fx = f(x0)
#         dfx = df(x0)

#         x1 = x0 - fx / dfx
#         error = abs(x1 - x0)

#         print(f"{i:<8} {x0:<15.8f} {fx:<16.8f} {error:.8e}")

#         if error < tol:
#             print("\nConverged\n")
#             print(f"Root = {x1}")
#             return x1

#         x0 = x1

#     print("\nDid not converge within maximum iterations.")
#     return None


# # Initial guess and tolerance
# initial_guess = 1.5
# tolerance = 1e-6

# newton_raphson(initial_guess, tolerance)

#transidental function
import math

def f(x):
    return x - math.cos(x)

def f_prime(x):
    return 1 + math.sin(x)

def newton_raphson(x0, tol, max_iter=20):
    print("Iter     Current x        f(x)              Error")
    print("---------------------------------------------------------")

    x = x0
    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = f_prime(x)
        x_new = x - fx / dfx
        error = abs(x_new - x)

        print(f"{i:<8} {x:<15.8f} {fx:<16.8f} {error:.8e}")

        if error < tol:
            print("\nConverged\n")
            print(f"Root = {x_new}")
            return x_new

        x = x_new

    print("\nDid not converge within maximum iterations.")
    return x


# Initial guess and tolerance
initial_guess = 0.5
tolerance = 1e-6

newton_raphson(initial_guess, tolerance)

