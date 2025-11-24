import numpy as np
import matplotlib.pyplot as plt

def computeCdf(P):
    return list(np.cumsum(P))

def plotCdfShow(X, F):
    plt.figure(figsize=(8, 5))
    plt.step(X, F, where="post")
    plt.xlabel("X")
    plt.ylabel("F(x)")
    plt.title("Функція розподілу F(x)")
    plt.grid(True)
    plt.show()

def plotCdfSave(X, F, filename="cdf.png"):
    plt.figure(figsize=(8, 5))
    plt.step(X, F, where="post")
    plt.xlabel("X")
    plt.ylabel("F(x)")
    plt.title("Функція розподілу F(x)")
    plt.grid(True)
    plt.savefig(filename)
    print(f"Графік F(x) збережено у {filename}")

