# ---------------------------------------------------------
# Error Correction Analysis of Numerical Errors
# Truncation Error, Round-off Error & Error Propagation
# ---------------------------------------------------------

import math

print("===== ERROR CORRECTION ANALYSIS OF NUMERICAL ERRORS =====")

# ---------------------------------------------------------
# Square root error example
# ---------------------------------------------------------
print("\n--- Square Root Error Example ---")
sqrt_error = math.sqrt(2) - 1.41421356
print("Error in sqrt(2):", sqrt_error)

# ---------------------------------------------------------
# Factorial Function
# ---------------------------------------------------------
print("\n--- Factorial Calculation ---")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

# ---------------------------------------------------------
# Ceiling and Floor Functions
# ---------------------------------------------------------
print("\n--- Ceiling and Floor Functions ---")
print("ceil(4.2)  =", math.ceil(4.2))
print("ceil(-5.8) =", math.ceil(-5.8))
print("floor(4.2) =", math.floor(4.2))
print("floor(-5.8)=", math.floor(-5.8))

# ---------------------------------------------------------
# Trigonometric Calculation
# ---------------------------------------------------------
print("\n--- Trigonometric Calculation ---")
print("sin(pi/2) =", math.sin(math.pi / 2))

# ---------------------------------------------------------
# Floating-Point Comparison Example
# ---------------------------------------------------------
print("\n--- Floating Point Comparison ---")

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

print("\nUsing tolerance comparison:")
print("math.isclose(a + b, c) :", math.isclose(a + b, c))

# ---------------------------------------------------------
# Floating Point Exact Value Demonstration
# ---------------------------------------------------------
print("\n--- Floating Point Precision Demonstration ---")

print("Stored values with .20f formatting:")
print(f"a = {a:.20f}")
print(f"b = {b:.20f}")
print(f"c = {c:.20f}")

sum_ab = a + b
difference = sum_ab - c

print("\na + b =", f"{sum_ab:.20f}")
print("a + b - c =", f"{difference:.20f}")

# ---------------------------------------------------------
# Simple Arithmetic Check
# ---------------------------------------------------------
print("\n--- Simple Arithmetic ---")
print("38 + 51.5 =", 38 + 51.5)

# ---------------------------------------------------------
# Numerical Error Analysis using Maclaurin Series
# ---------------------------------------------------------
print("\n===== NUMERICAL ERROR ANALYSIS =====")

x = 1
true_value = math.exp(x)
print("\nTrue value of e^1 =", true_value)

def maclaurin_exp(x, n):
    total = 0.0
    for k in range(n):
        total += (x ** k) / math.factorial(k)
    return total

print("\n--- Truncation Error (Maclaurin Series) ---")
for n in [1, 2, 3, 4, 5, 10]:
    approx = maclaurin_exp(x, n)
    error = abs(true_value - approx)
    print(f"Terms = {n:2d} | Approx = {approx:.8f} | Truncation Error = {error:.8f}")

# ---------------------------------------------------------
# Round-off Error using π
# ---------------------------------------------------------
print("\n--- Round-off Error Analysis ---")

pi_true = math.pi
roundings = [(3, round(pi_true, 3)),
             (5, round(pi_true, 5)),
             (10, round(pi_true, 10))]

for dec, val in roundings:
    abs_err = abs(pi_true - val)
    rel_err = abs_err / pi_true
    print(f"{dec} decimals: {val} | Abs Error = {abs_err:.12f} | Rel Error = {rel_err:.12e}")

# ---------------------------------------------------------
# Error Propagation Example
# ---------------------------------------------------------
print("\n--- Error Propagation Example ---")

a = 1e16
b = 1.0
result = a - (a - b)

print("Expected result = 1.0")
print("Computed result =", result)
print("Round-off Error =", abs(1.0 - result))

print("\n===== END OF PROGRAM =====")
