import math  
# Importing the math module.
# (Used in numerical methods; not directly required here but included as standard practice)

# -------------------------------------------------
# Defining the given function f(x)
# -------------------------------------------------
def f(x):
    # This function represents the equation:
    # f(x) = x^3 - x - 2
    # The root is the value of x for which f(x) = 0
    return x**3 - x - 2


# -------------------------------------------------
# Function to implement the Bisection Method
# -------------------------------------------------
def bisection_method(a, b, tol):
    # a  -> left endpoint of the interval
    # b  -> right endpoint of the interval
    # tol -> tolerance (maximum allowed error)

    # -------------------------------------------------
    # Checking the necessary condition for bisection
    # -------------------------------------------------
    # The function must change sign in the interval [a, b]
    if f(a) * f(b) >= 0:
        # If the sign does not change, root is not guaranteed
        print("Bisection method fails.")
        return None

    iteration = 1  # Counter to track number of iterations

    # Printing table header for interval values
    print("Iter\t a\t\t b\t\t midpoint\t f(midpoint)")
    print("-" * 70)

    # -------------------------------------------------
    # Iterative process of the Bisection Method
    # -------------------------------------------------
    # The loop continues until the error is less than tolerance
    # (b - a)/2 represents the maximum possible error
    while (b - a) / 2.0 > tol:

        # Calculate the midpoint of the interval
        midpoint = (a + b) / 2.0

        # Print the current interval and midpoint values
        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {midpoint:.6f}\t {f(midpoint):.6f}")

        # -------------------------------------------------
        # Check if the midpoint is the exact root
        # -------------------------------------------------
        if f(midpoint) == 0:
            # If f(midpoint) is zero, exact root is found
            return midpoint

        # -------------------------------------------------
        # Decide which sub-interval contains the root
        # -------------------------------------------------
        elif f(a) * f(midpoint) < 0:
            # Sign change occurs between a and midpoint
            # So the root lies in [a, midpoint]
            b = midpoint
        else:
            # Otherwise, the root lies in [midpoint, b]
            a = midpoint

        iteration += 1  # Increment iteration count

    # -------------------------------------------------
    # Final approximation of the root
    # -------------------------------------------------
    midpoint = (a + b) / 2.0

    # Print final interval values
    print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {midpoint:.6f}\t {f(midpoint):.6f}")

    # Return the approximate root
    return midpoint


# -------------------------------------------------
# Main Program
# -------------------------------------------------

# Initial interval values
a = 1    # Left endpoint
b = 2    # Right endpoint

# Tolerance value (accuracy up to 6 decimal places)
tolerance = 1e-6

# Calling the bisection method function
root = bisection_method(a, b, tolerance)

# -------------------------------------------------
# Displaying the final result
# -------------------------------------------------
if root is not None:
    print("\nFinal Result:")
    print(f"The root is approximately: {root:.6f}")
    print(f"f(root) = {f(root):.6f}")  # Verification that f(root) ≈ 0
