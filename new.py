# ============================================================
# NUMERICAL METHODS LAB
# Experiment: Analysis of Numerical Errors
# Topics Covered:
# 1. Truncation Error
# 2. Round-off Error
# 3. Taylor Series Approximation (sin x, e^x)
# 4. Floating Point Representation
# 5. Error Propagation
# ============================================================

import math

print("========== NUMERICAL ERROR ANALYSIS ==========")

# ------------------------------------------------------------
# 1. ROUND-OFF ERROR EXAMPLE (Square Root)
# ------------------------------------------------------------
print("\n--- Round-off Error using sqrt(2) ---")
approx_sqrt2 = math.sqrt(2)
given_value = 1.41421356
print("Difference =", approx_sqrt2 - given_value)

# ------------------------------------------------------------
# 2. FACTORIAL USING RECURSION
# ------------------------------------------------------------
print("\n--- Factorial using Recursion ---")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

# ------------------------------------------------------------
# 3. CEILING AND FLOOR FUNCTIONS
# ------------------------------------------------------------
print("\n--- Ceiling and Floor Functions ---")
print("ceil(4.2) =", math.ceil(4.2))
print("ceil(-5.8) =", math.ceil(-5.8))
print("floor(4.2) =", math.floor(4.2))
print("floor(-5.8) =", math.floor(-5.8))

# ------------------------------------------------------------
# 4. DEGREE TO RADIAN & BASIC sin(x)
# ------------------------------------------------------------
print("\n--- sin(pi/2) ---")
print("sin(pi/2) =", math.sin(math.pi / 2))

# ------------------------------------------------------------
# 5. FLOATING POINT COMPARISON ERROR
# ------------------------------------------------------------
print("\n--- Floating Point Comparison Error ---")

a = 0.1
b = 0.2
c = 0.3

print("a + b == c :", a + b == c)

print("\nExact stored values using repr():")
print("a =", repr(a))
print("b =", repr(b))
print("c =", repr(c))
print("a + b =", repr(a + b))

print("\nAfter rounding:")
print("round(a + b, 1) == c :", round(a + b, 1) == c)
print("Using math.isclose(a + b, c):", math.isclose(a + b, c))

# ------------------------------------------------------------
# 6. FLOATING POINT PRECISION DISPLAY
# ------------------------------------------------------------
print("\n--- Floating Point Precision (.20f) ---")
print(f"a = {a:.20f}")
print(f"b = {b:.20f}")
print(f"c = {c:.20f}")
print(f"a + b = {(a + b):.20f}")

# ------------------------------------------------------------
# 7. TRUNCATION ERROR: sin(x) USING TAYLOR SERIES (FROM FILE)
# ------------------------------------------------------------
print("\n--- Truncation Error for sin(x) (Taylor Series) ---")

# sin(x) ≈ x - x^3/3!
x = math.pi / 6  # 30 degrees
true_sin = math.sin(x)

approx_sin = x - (x ** 3) / math.factorial(3)

print("Actual sin(x) =", true_sin)
print("Approximation with 2 terms =", approx_sin)
print("Truncation Error =", abs(true_sin - approx_sin))

# ------------------------------------------------------------
# 8. sin(x) WITH MULTIPLE TERMS (FROM FILE)
# ------------------------------------------------------------
def taylor_sin(x, n_terms):
    return sum(((-1) ** n) * x ** (2 * n + 1) / math.factorial(2 * n + 1)
               for n in range(n_terms))

x_sin = math.pi / 4  # 45 degrees
true_sin = math.sin(x_sin)

print("\nTruncation Error Analysis for sin(x):")
for n in [2, 4, 6, 8]:
    approx = taylor_sin(x_sin, n)
    error = abs(true_sin - approx)
    print(f"Terms = {n}, Approx = {approx:.10f}, Error = {error:.10f}")

# ------------------------------------------------------------
# 9. TRUNCATION ERROR: e^x USING MACLAURIN SERIES (FROM FILE)
# ------------------------------------------------------------
print("\n--- Truncation Error for e^x (Maclaurin Series) ---")

def maclaurin_exp(x, n):
    s = 0.0
    for k in range(n):
        s += (x ** k) / math.factorial(k)
    return s

x = 1.0
true_exp = math.exp(x)

print("True value of e^1 =", true_exp)

for n in [2, 4, 6, 8, 10]:
    approx = maclaurin_exp(x, n)
    error = abs(true_exp - approx)
    print(f"Terms = {n}, Approx = {approx:.10f}, Error = {error:.10f}")

# ------------------------------------------------------------
# 10. ROUND-OFF ERROR USING PI ROUNDING
# ------------------------------------------------------------
print("\n--- Round-off Error using π ---")

pi_true = math.pi
for d in [3, 5, 10]:
    rounded = round(pi_true, d)
    abs_err = abs(pi_true - rounded)
    rel_err = abs_err / pi_true
    print(f"{d} decimals: {rounded} | Abs Error = {abs_err:.10e}, Rel Error = {rel_err:.10e}")

# ------------------------------------------------------------
# 11. ERROR PROPAGATION EXAMPLE
# ------------------------------------------------------------
print("\n--- Error Propagation Example ---")

a = 1e16
b = 1.0
c = a - (a - b)

print("Expected result = 1.0")
print("Computed result =", c)
print("Round-off Error =", abs(1.0 - c))

print("\n========== END OF PROGRAM ==========")
