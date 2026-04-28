import numpy as np

def gauss_elimination(A, B):
    n = len(B)

    # Form augmented matrix
    Aug = np.hstack((A, B.reshape(-1,1))).astype(float)

    print("Initial Augmented Matrix:")
    print(Aug)
    print("-" * 60)

    # Forward Elimination
    for i in range(n):
        print(f"\nPivot Position: Row {i+1}, Column {i+1}")
        

        if Aug[i][i] == 0:
            print("Pivot is zero. Checking for row swap...")
            for j in range(i+1, n):
                if Aug[j][i] != 0:
                    Aug[[i, j]] = Aug[[j, i]]
                    print(f"Swapped Row {i+1} with Row {j+1}")
                    print(Aug)
                    break
        
        print(f"Pivot Element = {Aug[i][i]}")
        

        for j in range(i+1, n):
            factor = Aug[j][i] / Aug[i][i]
            print(f"\nEliminating element at Row {j+1}, Column {i+1}")
            print(f"Factor = {factor}")
            print(f"R{j+1} = R{j+1} - ({factor}) * R{i+1}")
            
            Aug[j, i:] = Aug[j, i:] - factor * Aug[i, i:]
            
            print("Updated Matrix:")
            print(Aug)
        
        print("-" * 60)

    print("\nUpper Triangular Matrix:")
    print(Aug)
    print("=" * 60)


    X = np.zeros(n)
    print("\nBack Substitution Steps:")

    for i in range(n-1, -1, -1):
        sum_val = np.dot(Aug[i][i+1:n], X[i+1:n])
        X[i] = (Aug[i][-1] - sum_val) / Aug[i][i]

        print(f"\nCalculating variable at Row {i+1}")
        print(f"X[{i}] = ({Aug[i][-1]} - {sum_val}) / {Aug[i][i]}")
        print(f"X[{i}] = {X[i]}")

    return X




A = np.array([[1,1,1,1],
              [2,-1,3,2],
              [3,2,-1,1],
              [4,1,2,-2]])

B = np.array([10, 5, 7, 2])

solution = gauss_elimination(A, B)

print("\nFinal Solution:")
variables = ['x', 'y', 'z', 'u']
for i in range(len(solution)):
    print(f"{variables[i]} = {solution[i]:.4f}")