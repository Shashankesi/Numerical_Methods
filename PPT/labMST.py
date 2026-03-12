import math
def f(x):
    return 2*x - math.log10(x) - 7


def regula_falsi(a, b, eps=1e-6, max_iter=20):

    if f(a) * f(b) >= 0:
        print("Root not bracketed")
        return None

    print("Iter\t a\t\t b\t\t x\t\t f(x)")
    print("-"*60)

    for i in range(1, max_iter+1):

        fa = f(a)
        fb = f(b)
        x = (a*fb - b*fa) / (fb-fa)

        fx = f(x)

        print(f"{i}\t{a:.6f}\t{b:.6f}\t{x:.6f}\t{fx:.6f}")

        if abs(fx) < eps:
            print("\nRoot found!")
            return x

        if fa*fx < 0:
            b = x
        else:
            a = x

    return x
a = 3
b = 4

root = regula_falsi(a, b)

print("\nApproximate Root =", round(root,6))