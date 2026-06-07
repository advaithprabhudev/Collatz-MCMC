from residue import parity_vectors_from_residue_class, affine_constraint, count_odd, parity_vectors
from collatz import collatz_steps
import numpy as np
import scipy.linalg as sp

# Making the Exact Transition Matrix

def ex_transition_matrix(k) -> np.ndarray:
    m = 2 ** k
    p = np.zeros((m, m))

    for i in range(m):
        v = parity_vectors(i, k)
        s = count_odd(v)
        c = affine_constraint(v)
        j = (3 ** s * i + c) % m
        p[i][j] = 1.0
    return p

# Empirical Transition Matrix

def em_transition_matrix(n, k) -> np.ndarray:
    m = 2 ** k
    c = np.zeros((m, m))
    p = np.zeros((m, m))
    for _ in range(1, n+1):
        i = n % m
        j = collatz_steps(n) % m
        c[i][j] +=  1
    
    for h in range(m):
        if c[i].sum() > 0:
            p[i] = c[i] / c[i].sum()
        else:
            p[i] = np.full(m, 1.0 / m)
    return p

# Stationary Distributions of Markov Chains

def stationary_dsitribution(p) -> np.ndarray:
        eigenvalues, eigenvectors = np.linalg.eig(p.T)
        idx = np.argmin(np.abs(eigenvalues - 1.0))
        pi = np.real(eigenvalues[:,  idx])
        if np.all(pi < 0):
            pi = -pi
        pi = pi / pi.sum()
        return pi

# Irreducibility of Markov Property

def is_irreducible(p : np.ndarray):
    m = p.shape[0]
    r = np.linalg.matrix_power(np.eye(m) + p, m)
    return bool(np.all(r > 0))

# Aperiodicity of Markov Property

def is_aperiodic(p)



    