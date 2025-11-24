def inputDistribution():
    print("Введіть значення X через пробіл:")
    X = list(map(float, input().split()))

    print("Введіть відповідні ймовірності P через пробіл:")
    P = list(map(float, input().split()))

    return X, P
