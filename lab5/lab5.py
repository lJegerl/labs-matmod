import numpy as np
import matplotlib.pyplot as plt

A_matrix = np.array([[0.7, -0.3, -0.2],
                     [-0.2, 0.2, -0.7],
                     [-0.5, 0.1, 2]])
A = np.eye(3) - A_matrix
f_vector = np.array([-1, -3, 8])
actual_solution = [-3.07018, 1.14035, 2.45614]

def solve(A, f, num_chains, chain_length):
    n = A.shape[0]
    x = np.zeros(n)

    for j in range(n):
        for _ in range(num_chains):
            weight = 1
            state_prev = j
            state_new = 0
            x[j] += f[j]

            for _ in range(chain_length):
                state_new = np.random.choice(n)
                weight *= n * A[state_prev][state_new]
                x[j] += weight * f[state_new]
                state_prev = state_new

    return x / num_chains

num_chains_set = [10, 30, 60, 100]
chain_length_set = [10, 100, 300, 1000]

results = {}

for num_chains in num_chains_set:
    for chain_length in chain_length_set:
        computed_solution = solve(A, f_vector, num_chains, chain_length)
        print(f'{num_chains} {chain_length}')
        print(f'Computed: {computed_solution}')
        print(f'Actual: {actual_solution}\n')

        error = np.linalg.norm(computed_solution - actual_solution)
        results[(num_chains, chain_length)] = error

plt.figure(figsize=(14, 7))

for num_chains in num_chains_set:
    errors = [results[(num_chains, cl)] for cl in chain_length_set]
    plt.plot(chain_length_set, errors, label=f'Num Chains: {num_chains}')