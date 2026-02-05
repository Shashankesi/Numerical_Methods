import math

# Function to evaluate polynomial f(x)
def f(x, coeff):
    degree = len(coeff) - 1
    result = 0
    for i in range(len(coeff)):
        result += coeff[i] * (x ** (degree - i))
    return result


def regula_falsi(coeff, a, b, eps=1e-6, max_iter=100):
    # Condition: Root must be bracketed
    if f(a, coeff) * f(b, coeff) >= 0:
        print("Regula Falsi method fails: root not bracketed.")
        return None

    print("Iter\t a\t\t b\t\t x\t\t f(x)")
    print("-" * 60)

    for i in range(1, max_iter + 1):
        fa = f(a, coeff)
        fb = f(b, coeff)

        # Regula Falsi formula
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x, coeff)

        print(f"{i}\t{a:.6f}\t{b:.6f}\t{x:.6f}\t{fx:.6f}")

        # Stopping condition
        if abs(fx) < eps:
            print("\nRoot found!")
            return x

        # Interval update
        if fa * fx < 0:
            b = x
        else:
            a = x

    print("\nMethod did not converge within given iterations.")
    return None


# ------------------ Example ------------------
# Polynomial: x^3 - 2x - 5 = 0
coeff = [1, 0, -2, -5]

a = 2
b = 3
epsilon = 1e-6
max_iterations = 20

root = regula_falsi(coeff, a, b, epsilon, max_iterations)

if root is not None:
    print(f"\nApproximate root = {root:.6f}")
