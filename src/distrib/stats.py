import numpy as np

def computeCharacteristics(X, P):
    X = np.array(X)
    P = np.array(P)

    M = np.sum(X * P)
    D = np.sum((X**2) * P) - M**2
    sigma = np.sqrt(D)

    maxP = np.max(P)
    modes = [float(m) for m in X[P == maxP]]

    return M, D, sigma, modes

