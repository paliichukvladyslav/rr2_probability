import matplotlib

backend = matplotlib.get_backend()

import matplotlib.pyplot as plt

def plotPolygonShow(X, P):
    plt.figure(figsize=(8, 5))
    plt.plot(X, P, marker='o')
    plt.xlabel("X")
    plt.ylabel("P(X)")
    plt.title("Багатокутник розподілу")
    plt.grid(True)
    plt.show()

def plotPolygonSave(X, P, filename="polygon.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(X, P, marker='o')
    plt.xlabel("X")
    plt.ylabel("P(X)")
    plt.title("Багатокутник розподілу")
    plt.grid(True)
    plt.savefig(filename)
    print(f"Графік збережено у файл {filename}")
