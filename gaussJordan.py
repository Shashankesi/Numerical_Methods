import numpy as np

def gauss_jordan(A, B):
    n = len(B)

    # Form augmented matrix
    Aug = np.hstack((A, B.reshape(-1,1))).astype(float)

    print("Initial Augmented Matrix:")
    print(Aug)
    print("-" * 60)

    for i in range(n):

        print(f"\nPivot Position: Row {i+1}, Column {i+1}")

        # Check for zero pivot
        if Aug[i][i] == 0:
            print("Pivot is zero. Checking for row swap...")
            for j in range(i+1, n):
                if Aug[j][i] != 0:
                    Aug[[i, j]] = Aug[[j, i]]
                    print(f"Swapped Row {i+1} with Row {j+1}")
                    print(Aug)
                    break

        pivot = Aug[i][i]
        print(f"Pivot Element = {pivot}")

        # Make pivot = 1
        Aug[i] = Aug[i] / pivot
        print(f"\nR{i+1} = R{i+1} / {pivot}")
        print("Matrix after making pivot 1:")
        print(Aug)

        # Make other elements in column = 0
        for j in range(n):
            if j != i:
                factor = Aug[j][i]
                print(f"\nEliminating element at Row {j+1}, Column {i+1}")
                print(f"Factor = {factor}")
                print(f"R{j+1} = R{j+1} - ({factor}) * R{i+1}")

                Aug[j] = Aug[j] - factor * Aug[i]

                print("Updated Matrix:")
                print(Aug)

        print("-" * 60)

    print("\nReduced Row Echelon Form (Gauss-Jordan Result):")
    print(Aug)
    print("=" * 60)

    # Extract solution
    X = Aug[:, -1]

    return X


# Example 4-variable system:
#  x +  y +  z +  u = 10
# 2x -  y + 3z + 2u = 5
# 3x + 2y -  z +  u = 7
# 4x +  y + 2z - 2u = 2

A = np.array([
    [1, 1, 1, 1],
    [2, -1, 3, 2],
    [3, 2, -1, 1],
    [4, 1, 2, -2]
])

B = np.array([10, 5, 7, 2])

solution = gauss_jordan(A, B)

print("\nFinal Solution:")
variables = ['x', 'y', 'z', 'u']
for i in range(len(solution)):
    print(f"{variables[i]} = {solution[i]:.4f}")