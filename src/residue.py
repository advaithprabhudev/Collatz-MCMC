from collatz import collatz_steps
import numpy as np

# Implementing Initial Collatz Residue Class


def residue_class(n, k):
    return n % (2 ** k)

# Parity Vectors implementation


def parity_vectors(n, steps):
    x = []
    for i in range(1, steps + 1):
        x.append(int(n % 2))
        n = collatz_steps(n)
    return x

# Parity Vectors deduction from Residue Classes


def parity_vectors_from_residue_class(r, f):
    vector = []
    x = r
    for _ in range(1, f + 1):
        vector.append(x % 2)
        x = collatz_steps(x)
    return vector

# Counting the alternate steps


def count_odd(parity_vec):
    return np.sum(parity_vec)

# Affine Constraint


def affine_constraint(parity_vec):
    k = len(parity_vec)
    c = 0
    for i in range(k):
        if parity_vec[i] == 1:
            s = np.sum(parity_vec[i+1:])
            c += 3 ** s
    return c

# Partition of Residue


def partition_residue(n, k):
    m = 2 ** k
    return [i % m for i in range(1, n+1)]
