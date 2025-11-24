from distrib.input import inputDistribution
from utils.menu import menu

def main():
    X, P = inputDistribution()
    menu(X, P)

if __name__ == "__main__":
    main()
