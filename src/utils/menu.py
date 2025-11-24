from distrib.polygon import *

def menu(X, P):
    while True:
        print("\nМеню:")
        print("[1] Показати ряд розподілу")
        print("[2] Побудувати багатокутник розподілу")
        print("[3] Зберегти багатокутник у файл")
        print("[0] Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("X =", X)
            print("P =", P)
        elif choice == "2":
            plotPolygonShow(X, P)
        elif choice == "3":
            plotPolygonSave(X, P)
        elif choice == "0":
            print("Завершення роботи...")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
