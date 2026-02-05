# # Error corrction Analysis of Numerical Errors: Truncation and Round-off
# #Behavioral Analysis of Numerical Errors
# import math
# math.sqrt(2) - 1.41421356

# #find 5 factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))
# #celling and floor fucntions
# print(math.ceil(4.2))
# print(math.ceil(-5.8))
# print(math.floor(4.2))
# print(math.floor(-5.8))

# #coverting degrees to radians and vice versa
# #calculate sin pei/2
# print(math.sin(math.pi / 2))

# # if a=0.1, b=0.2 , c=0.3 then check a+b==c
# a = 0.1
# b=0.2
# c=0.3
# print(a + b == c)

# # print the value of all a b and c full value why is it false
# print(repr(a))
# print(repr(b))
# print(repr(c))
# print(repr(a + b))

# print(round(a + b, 1) == c)

# # Floating point exact value and round-off error demonstration

# # Floating point exact value, .20f formatting, and round-off error demonstration



# #Define values
# a = 0.1
# b = 0.2
# c = 0.3

# #   Print exact stored values using repr()
# print("Exact stored values (repr):")
# print("a =", repr(a))
# print("b =", repr(b))
# print("c =", repr(c))

# print("\n--------------------------------")

# #Print values using .20f formatting
# print("Stored values with .20f formatting:")
# print(f"a = {a:.20f}")
# print(f"b = {b:.20f}")
# print(f"c = {c:.20f}")

# print("\n--------------------------------")

# #Calculate a + b
# sum_ab = a + b
# print("Exact value of a + b (repr) =", repr(sum_ab))
# print(f"a + b with .20f = {sum_ab:.20f}")

# print("\n--------------------------------")

# #Calculate difference (a + b - c)
# difference = sum_ab - c
# print("Exact difference (repr) =", repr(difference))
# print(f"a + b - c with .20f = {difference:.20f}")

# print("\n--------------------------------")

# #Direct comparison
# print("Direct comparison (a + b == c):", a + b == c)

# print("\n--------------------------------")

# # Handle round-off error using rounding
# print("After rounding (round(a + b, 1) == c):", round(sum_ab, 1) == c)

# print("\n--------------------------------")

# # Best practice comparison using tolerance
# print("Using math.isclose(a + b, c):", math.isclose(a + b, c))

# print(38+51.5)



import math

print("----- NUMERICAL ERROR ANALYSIS -----")

# -----------------------------------
# True value
# -----------------------------------
x = 1
true_value = math.exp(x)
print(f"\nTrue value of e^1 = {true_value}")

# -----------------------------------
# Truncation Error using Maclaurin Series
# -----------------------------------
def maclaurin_exp(x, n):
    s = 0.0
    for k in range(n):
        s += (x ** k) / math.factorial(k)
    return s

print("\n--- Truncation Error Analysis ---")
for n in [1, 2, 3, 4, 5, 10]:
    approx = maclaurin_exp(x, n)
    error = abs(true_value - approx)
    print(f"Terms = {n}, Approx = {approx:.7f}, Truncation Error = {error:.7f}")

# -----------------------------------
# Round-off Error Analysis
# -----------------------------------
print("\n--- Round-off Error Analysis ---")

pi_true = math.pi

pi_3 = round(pi_true, 3)
pi_5 = round(pi_true, 5)
pi_10 = round(pi_true, 10)

round_data = [
    ("3 decimal", pi_3),
    ("5 decimal", pi_5),
    ("10 decimal", pi_10)
]

for label, val in round_data:
    abs_err = abs(pi_true - val)
    rel_err = abs_err / pi_true
    print(f"{label}: {val} | Abs Error = {abs_err:.10f}, Rel Error = {rel_err:.13e}")

# -----------------------------------
# Error Propagation Example
# -----------------------------------
print("\n--- Error Propagation Example ---")

a = 1e16
b = 1.0
c = a - (a - b)

print(f"Expected result = 1.0, Computed result = {c}")
print(f"Round-off Error = {abs(1.0 - c)}")
