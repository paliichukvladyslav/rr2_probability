from distrib.polygon import plotPolygonShow, plotPolygonSave
from distrib.cdf import computeCdf, plotCdfShow, plotCdfSave
from distrib.stats import computeCharacteristics

def menu(X, P):
    while True:
        print("\nМеню:")
        print("[1] Показати ряд розподілу")
        print("[2] Побудувати багатокутник розподілу")
        print("[3] Зберегти багатокутник у файл")
        print("[4] Побудувати графік F(x)")
        print("[5] Зберегти графік F(x) у файл")
        print("[6] Обчислити M, D, σ, Mo")
        print("[0] Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("X =", X)
            print("P =", P)
        elif choice == "2":
            plotPolygonShow(X, P)
        elif choice == "3":
            plotPolygonSave(X, P)
        elif choice == "4":
            F = computeCdf(P)
            plotCdfShow(X, F)
        elif choice == "5":
            F = computeCdf(P)
            plotCdfSave(X, F)
        elif choice == "6":
            M, D, sigma, modes = computeCharacteristics(X, P)
            print(f"M = {M}")
            print(f"D = {D}")
            print(f"σ = {sigma}")
            print(f"Мода(и): {modes}")
        elif choice == "0":
            print("Завершення роботи...")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
