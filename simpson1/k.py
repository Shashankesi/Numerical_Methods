import numpy as np

def gauss(A, B):
    n = len(B)
    Aug = np.hstack((A, B.reshape(-1,1))).astype(float)

    for i in range(n):
        for j in range(i+1, n):
            factor = Aug[j][i] / Aug[i][i]
            Aug[j, i:] -= factor * Aug[i, i:]
  
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (Aug[i][-1] - np.dot(Aug[i][i+1:n], X[i+1:n])) / Aug[i][i]

    return X



A = np.array([[1,1,1,1],
              [2,-1,3,2],
              [3,2,-1,1],
              [4,1,2,-2]])

B = np.array([10,5,7,2])

sol = gauss(A, B)


print("\n --    --")
print("\n     ;   ")
print("\n   ----  ")
print("\nFinal Solution:")
variables = ['x', 'y', 'z', 'u']
for i in range(len(sol)):
    print(f"{variables[i]} = {sol[i]:.4f}")