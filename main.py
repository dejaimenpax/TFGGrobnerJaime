# main.py
from polynomial import Polynomial


def main():

    # EJEMPLO 3-COLOREADO
    p_ejemplo = Polynomial("abcde", "a^3-3a^2+2a")

    grafo_ejemplo = [
        p_ejemplo,
        Polynomial("abcde", "b^3 - 3b^2 + 2b"),
        Polynomial("abcde", "c^3 - 3c^2 + 2c"),
        Polynomial("abcde", "d^3 - 3d^2 + 2d"),
        Polynomial("abcde", "e^3 - 3e^2 + 2e"),
        Polynomial("abcde", "a^2 + ab + b^2 - 3a - 3b + 2"),
        Polynomial("abcde", "a^2 + ac + c^2 - 3a - 3c + 2"),
        Polynomial("abcde", "b^2 + bd + d^2 - 3b - 3d + 2"),
        Polynomial("abcde", "b^2 + be + e^2 - 3b - 3e + 2"),
        Polynomial("abcde", "d^2 + de + e^2 - 3d - 3e + 2"),
    ]

    '''
    grobner_basis = p_ejemplo.calculate_grobner_bases(grafo_ejemplo)
    print("\nLa base obtenida G es:")
    for p in gobner_basis:
        print(p.read_polynomial())
    '''

    reduced_ejemplo = p_ejemplo.reduce_grobner(grafo_ejemplo)
    print("\nReduced Grobner basis:")
    for p in reduced_ejemplo:
        print(p.read_polynomial())

    # EJEMPLO 2-COLOREADO
    p_2coloreado = Polynomial("abcde", "a^2 - a")

    grafo_2coloreado = [
        p_2coloreado,
        Polynomial("abcde", "b^2 - b"),
        Polynomial("abcde", "c^2 - c"),
        Polynomial("abcde", "d^2 - d"),
        Polynomial("abcde", "e^2 - e"),
        Polynomial("abcde", "a + b - 1"),
        Polynomial("abcde", "a + c - 1"),
        Polynomial("abcde", "b + d - 1"),
        Polynomial("abcde", "b + e - 1"),
        Polynomial("abcde", "d + e - 1"),
    ]

    calculated_grobner_2coloreado = p_2coloreado.calculate_grobner_bases(
        grafo_2coloreado)
    print("\nGrobner basis:")
    for p in calculated_grobner_2coloreado:
        print(p.read_polynomial())

    reduced_2coloreado = p_2coloreado.reduce_grobner(
        calculated_grobner_2coloreado)
    print("\nReduced Grobner basis:")
    for p in reduced_2coloreado:
        print(p.read_polynomial())


if __name__ == "__main__":
    main()
