import numpy as np

# Function to compute divided differences
def divided_difference(x, y):
    n = len(x)
    coef = y.astype(float).copy()

    print("\n========== DIVIDED DIFFERENCE TABLE ==========\n")
    print("Initial Coefficients (y values):")
    print(coef, "\n")

    for j in range(1, n):
        print(f"Iteration {j}:")
        for i in range(j, n):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
        print(f"Coefficients after iteration {j}: {coef}\n")

    return coef


# Function to evaluate Newton Polynomial
def newton_polynomial(coef, x_data, x):
    n = len(coef)
    result = coef[0]
    product = 1.0

    print("\n========== NEWTON POLYNOMIAL EVALUATION ==========\n")
    print(f"Evaluating at x = {x}\n")

    for i in range(1, n):
        product *= (x - x_data[i-1])
        term = coef[i] * product
        result += term

        print(f"Step {i}:")
        print(f"  Product = {product:.4f}")
        print(f"  Term    = {coef[i]:.4f} × {product:.4f} = {term:.4f}")
        print(f"  Result  = {result:.4f}\n")

    return result


# 🔷 Degree 3 data (Cubic: y = x^3)
x_data = np.array([0, 1, 2, 3])
y_data = np.array([0, 1, 8, 27])

# Point to evaluate
x_value = 2.5


# Compute coefficients
coefficients = divided_difference(x_data, y_data)

print("Final Coefficients:")
print(coefficients)


# Evaluate polynomial
y_value = newton_polynomial(coefficients, x_data, x_value)


# 🔷 Calculate degree
degree = len(x_data) - 1


# 🔷 Final Output Summary
print("\n========== FINAL OUTPUT ==========\n")
print("Given Data Points:")
for i in range(len(x_data)):
    print(f"  x = {x_data[i]}, y = {y_data[i]}")

print(f"\nInterpolated Value:")
print(f"  At x = {x_value}, y = {y_value:.4f}")

print(f"\nFunction Degree: {degree}")