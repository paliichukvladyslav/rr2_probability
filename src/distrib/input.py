def inputDistribution():
    print("Введіть значення X через пробіл:")
    X = list(map(float, input().split()))

    print("Введіть відповідні ймовірності P через пробіл:")
    P = list(map(float, input().split()))

    if len(X) != len(P):
      raise ValueError("К-сть значень X і P повинна збігатися.")

    total_p = sum(P)
    if abs(total_p - 1) > 1:
        raise ValueError(f"Сума ймовірностей дорівнює {total_p}, а повинна дорівнювати 1.")

    return X, P
