# main.py
from polynomial import Polynomial


def main():
    '''
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

    '''
    grobner_basis = p_ejemplo.calculate_grobner_bases(grafo_ejemplo)
    print("\nLa base obtenida G es:")
    for p in gobner_basis:
        print(p.read_polynomial())
    '''

    '''
    reduced_ejemplo = p_ejemplo.reduce_grobner(grafo_ejemplo)
    print("\nReduced Grobner basis:")
    for p in reduced_ejemplo:
        print(p.read_polynomial())
    '''

    # EJEMPLO HORARIOS

    p_horario =  Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "a^4 - 6a^3 + 11a^2 - 6a")

    grafo_horarios = [
        p_horario,
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "b^4 - 6b^3 + 11b^2 - 6b"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "c^4 - 6c^3 + 11c^2 - 6c"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "d^4 - 6d^3 + 11d^2 - 6d"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "e^4 - 6e^3 + 11e^2 - 6e"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "f^4 - 6f^3 + 11f^2 - 6f"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "g^4 - 6g^3 + 11g^2 - 6g"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "h^4 - 6h^3 + 11h^2 - 6h"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "i^4 - 6i^3 + 11i^2 - 6i"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "j^4 - 6j^3 + 11j^2 - 6j"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "k^4 - 6k^3 + 11k^2 - 6k"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "l^4 - 6l^3 + 11l^2 - 6l"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "m^4 - 6m^3 + 11m^2 - 6m"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "n^4 - 6n^3 + 11n^2 - 6n"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "o^4 - 6o^3 + 11o^2 - 6o"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "p^4 - 6p^3 + 11p^2 - 6p"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "q^4 - 6q^3 + 11q^2 - 6q"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "r^4 - 6r^3 + 11r^2 - 6r"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "s^4 - 6s^3 + 11s^2 - 6s"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "t^4 - 6t^3 + 11t^2 - 6t"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "u^4 - 6u^3 + 11u^2 - 6u"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "v^4 - 6v^3 + 11v^2 - 6v"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "w^4 - 6w^3 + 11w^2 - 6w"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "x^4 - 6x^3 + 11x^2 - 6x"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "y^4 - 6y^3 + 11y^2 - 6y"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "z^4 - 6z^3 + 11z^2 - 6z"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "A^4 - 6A^3 + 11A^2 - 6A"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "B^4 - 6B^3 + 11B^2 - 6B"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "C^4 - 6C^3 + 11C^2 - 6C"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "D^4 - 6D^3 + 11D^2 - 6D"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "E^4 - 6E^3 + 11E^2 - 6E"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "F^4 - 6F^3 + 11F^2 - 6F"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "G^4 - 6G^3 + 11G^2 - 6G"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "H^4 - 6H^3 + 11H^2 - 6H"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "I^4 - 6I^3 + 11I^2 - 6I"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "J^4 - 6J^3 + 11J^2 - 6J"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "K^4 - 6K^3 + 11K^2 - 6K"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "L^4 - 6L^3 + 11L^2 - 6L"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "M^4 - 6M^3 + 11M^2 - 6M"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "N^4 - 6N^3 + 11N^2 - 6N"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "O^4 - 6O^3 + 11O^2 - 6O"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "P^4 - 6P^3 + 11P^2 - 6P"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "Q^4 - 6Q^3 + 11Q^2 - 6Q"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "R^4 - 6R^3 + 11R^2 - 6R"),
        
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "I^3 + QI^2 - 6I^2 + IQ^2 - 6IQ + 11I + Q^3 + 11Q - 6Q^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "k^3 + ok^2 - 6k^2 + ko^2 - 6ko + 11k + o^3 + 11o - 6o^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "k^3 + wk^2 - 6k^2 + kw^2 - 6kw + 11k + w^3 + 11w - 6w^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "o^3 + wo^2 - 6o^2 + ow^2 - 6ow + 11o + w^3 + 11w - 6w^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "M^3 + kM^2 - 6M^2 + Mk^2 - 6Mk + 11M + k^3 + 11k - 6k^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "M^3 + wM^2 - 6M^2 + Mw^2 - 6Mw + 11M + w^3 + 11w - 6w^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "M^3 + oM^2 - 6M^2 + Mo^2 - 6Mo + 11M + o^3 + 11o - 6o^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "g^3 + Eg^2 - 6g^2 + gE^2 - 6gE + 11g + E^3 + 11E - 6E^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "g^3 + Kg^2 - 6g^2 + gK^2 - 6gK + 11g + K^3 + 11K - 6K^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "E^3 + KE^2 - 6E^2 + EK^2 - 6EK + 11E + K^3 + 11K - 6K^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "G^3 + OG^2 - 6G^2 + GO^2 - 6GO + 11G + O^3 + 11O - 6O^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "e^3 + Ae^2 - 6e^2 + eA^2 - 6eA + 11e + A^3 + 11A - 6A^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "a^3 + ya^2 - 6a^2 + ay^2 - 6ay + 11a + y^3 + 11y - 6y^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "f^3 + Bf^2 - 6f^2 + fB^2 - 6fB + 11f + B^3 + 11B - 6B^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "f^3 + Lf^2 - 6f^2 + fL^2 - 6fL + 11f + L^3 + 11L - 6L^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "f^3 + if^2 - 6f^2 + fi^2 - 6fi + 11f + i^3 + 11i - 6i^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "B^3 + LB^2 - 6B^2 + BL^2 - 6BL + 11B + L^3 + 11L - 6L^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "L^3 + iL^2 - 6L^2 + Li^2 - 6Li + 11L + i^3 + 11i - 6i^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "i^3 + Bi^2 - 6i^2 + iB^2 - 6iB + 11i + B^3 + 11B - 6B^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "b^3 + Pb^2 - 6b^2 + bP^2 - 6bP + 11b + P^3 + 11P - 6P^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "b^3 + Nb^2 - 6b^2 + bN^2 - 6bN + 11b + N^3 + 11N - 6N^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "b^3 + Hb^2 - 6b^2 + bH^2 - 6bH + 11b + H^3 + 11H - 6H^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "P^3 + NP^2 - 6P^2 + PN^2 - 6PN + 11P + N^3 + 11N - 6N^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "N^3 + HN^2 - 6N^2 + NH^2 - 6NH + 11N + H^3 + 11H - 6H^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "H^3 + PH^2 - 6H^2 + HP^2 - 6HP + 11H + P^3 + 11P - 6P^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "c^3 + mc^2 - 6c^2 + cm^2 - 6cm + 11c + m^3 + 11m - 6m^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "c^3 + zc^2 - 6c^2 + cz^2 - 6cz + 11c + z^3 + 11z - 6z^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "m^3 + zm^2 - 6m^2 + mz^2 - 6mz + 11m + z^3 + 11z - 6z^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "d^3 + pd^2 - 6d^2 + dp^2 - 6dp + 11d + p^3 + 11p - 6p^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "d^3 + Rd^2 - 6d^2 + dR^2 - 6dR + 11d + R^3 + 11R - 6R^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "p^3 + Rp^2 - 6p^2 + pR^2 - 6pR + 11p + R^3 + 11R - 6R^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "h^3 + nh^2 - 6h^2 + hn^2 - 6hn + 11h + n^3 + 11n - 6n^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "h^3 + Fh^2 - 6h^2 + hF^2 - 6hF + 11h + F^3 + 11F - 6F^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "n^3 + Fn^2 - 6n^2 + nF^2 - 6nF + 11n + F^3 + 11F - 6F^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "G^3 + lG^2 - 6G^2 + Gl^2 - 6Gl + 11G + l^3 + 11l - 6l^2 - 6"),
        Polynomial("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "O^3 + lO^2 - 6O^2 + Ol^2 - 6Ol + 11O + l^3 + 11l - 6l^2 - 6"),


     
    ]

    reduced_horarios = p_horario.reduce_grobner(grafo_horarios)
    print("\nReduced Grobner basis:")
    for p in reduced_horarios:
        print(p.read_polynomial())


if __name__ == "__main__":
    main()
