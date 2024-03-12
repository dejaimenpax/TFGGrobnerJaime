from monomial import Monomial


class Polynomial:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            self.monomials = args[0]
        elif len(args) == 0:
            self.monomials = []
        elif len(args) == 1 and isinstance(args[0], Monomial):
            self.monomials = [args[0]]
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            variables = args[0]
            p = args[1]
            n_variables = len(variables)
            monomios = []

            p_array = p.split()
            monomio_anterior = ""

            for monomio in p_array:
                if monomio != "+" and monomio != "-":
                    # Creamos los exponentes vacíos
                    exponentes = [0] * n_variables
                    coeficiente = ""

                    if monomio_anterior == "-":
                        coeficiente = "-"

                    i = 0
                    while i < len(monomio):
                        caracter = monomio[i]

                        # Verificar si los elementos iniciales son números
                        if caracter.isdigit() or caracter == "-":
                            coeficiente += caracter
                        else:
                            # Verificar si el elemento es igual a alguna de las variables
                            var = -1
                            encontrada = False

                            while not encontrada and var < (n_variables - 1):
                                var += 1
                                encontrada = caracter == variables[var]

                            # Si encontramos la variable
                            if encontrada:
                                if i + 1 < len(monomio) and monomio[i + 1] == '^':
                                    exp = int(monomio[i + 2])
                                    exponentes[var] = exp
                                    i += 2
                                else:
                                    exponentes[var] = 1

                        i += 1

                    if coeficiente == "":
                        coeficiente = "1"
                    elif coeficiente == "-":
                        coeficiente = "-1"

                    # Convertir el número en una fracción
                    coef = [int(coeficiente), 1]
                    m = Monomial(coef, exponentes)
                    monomios.append(m)

                monomio_anterior = monomio

            self.monomials = monomios

        elif len(args) == 1 and isinstance(args[0], int):
            max_exp = args[0]
            d = [0] * max_exp
            coef = [0, 0]
            m = Monomial(coef, d)
            self.monomials = [m]

    def simplify(self):
        unique_monomials = set(self.monomials)
        terms_equal = True
        while terms_equal:
            terms_equal = False
            for m1 in unique_monomials.copy():
                for m2 in unique_monomials.copy():
                    if m1 != m2 and m1.m_exp == m2.m_exp:
                        # Sumar los coeficientes de los monomios sin cambiar el signo
                        sum_coefficient = [m1.coefficient[0] +
                                           m2.coefficient[0], m1.coefficient[1]]
                        sum_monomial = Monomial(sum_coefficient, m1.m_exp)
                        unique_monomials.remove(m1)
                        unique_monomials.remove(m2)
                        unique_monomials.add(sum_monomial)
                        terms_equal = True
                        break
                if terms_equal:
                    break

        # Eliminar los monomios con coeficiente cero
        unique_monomials = {
            m for m in unique_monomials if m.coefficient[0] != 0 or not m.m_exp}
        self.monomials = list(unique_monomials)

        # Ordenar los monomios según el orden lexicográfico
        self.monomials.sort(key=lambda m: m.m_exp)

        return Polynomial(self.monomials)

    def lt_polynomial(self):
        self.simplify()
        superior = self.monomials[0]
        for i in range(1, len(self.monomials)):
            actual = self.monomials[i]
            superior = superior.lex(actual)
        return superior

    def lc_polynomial(self):
        leading_term = self.lt_polynomial()
        return leading_term.coefficient

    def lp_polynomial(self):
        leading_term = self.lt_polynomial()
        return Monomial([1, 1], leading_term.m_exp)

    def read_polynomial(self):
        sb = []
        first_term = True
        for m in self.monomials:
            if (m.coefficient[0] > 0 and m.coefficient[1] > 0) or (m.coefficient[0] < 0 and m.coefficient[1] < 0):
                if not first_term:
                    sb.append(" + ")
                sb.append(m.read_monomial())
                first_term = False
            elif m.coefficient[0] < 0 or m.coefficient[0] < 0:
                sb.append(" " + m.read_monomial())
                first_term = False
        return ''.join(sb)

    def add_polynomial(self, p):
        self.simplify()
        p.simplify()

        res = []
        for m1 in self.monomials:
            matched = False
            for m2 in p.monomials:
                if m1.m_exp == m2.m_exp:
                    matched = True
                    coef = m1.sum_fraction(m1.coefficient, m2.coefficient)
                    if coef[0] != 0:
                        new_monomial = Monomial(coef, m1.m_exp)
                        res.append(new_monomial)
                    break
            if not matched:
                res.append(m1)
        for m1 in p.monomials:
            matched = False
            for m2 in self.monomials:
                if m1.m_exp == m2.m_exp:
                    matched = True
                    break
            if not matched:
                res.append(m1)
        return Polynomial(res).simplify()

    def subtract_polynomial(self, p):
        p1 = Polynomial(self.monomials)
        p2 = Polynomial(p.monomials)

        for m in p2.monomials:
            m.coefficient[0] *= -1
        return p1.add_polynomial(p2).simplify()

    def multiply_polynomials(self, p):
        self.simplify()
        p.simplify()

        res_monomials = []
        for m1 in self.monomials:
            for m2 in p.monomials:
                res_monomials.append(m1.multiply_monomials(m2))
        return Polynomial(res_monomials).simplify()

    def univariate_division(self, g):
        self.simplify()
        g.simplify()

        var = 0
        for monomial in self.monomials:
            if len(monomial.m_exp) > var:
                var = len(monomial.m_exp)
        q = Polynomial(var)
        r = self
        r_empty = False
        r_degree = r.lp_polynomial().exp_sum()

        while not r_empty and r_degree >= g.lp_polynomial().exp_sum():
            m_sum = r.lt_polynomial().division_monomials(g.lt_polynomial())
            p_sum = Polynomial([m_sum])

            q = q.add_polynomial(p_sum)

            p_sub = p_sum.multiply_polynomials(g)
            for monomial in p_sub.monomials:
                monomial.coefficient[0] *= -1
            r = r.add_polynomial(p_sub)

            r_empty = not r.monomials
            r_degree = r.lp_polynomial().exp_sum()

        q.simplify()
        r.simplify()

        return q, r

    def euclidean_algorithm(self, p):
        f = self
        g = p
        g_empty = False
        while not g_empty:
            f.simplify()
            g.simplify()
            division = f.univariate_division(g)

            f = g
            g = division[1]

            g_empty = True
            if g.monomials:
                for m in g.monomials:
                    for i in m.m_exp:
                        if i != 0:
                            g_empty = False
                if g_empty:
                    for m in g.monomials:
                        if m.coefficient[0] != 0 or m.coefficient[1] != 0:
                            g_empty = False

        lc_pol = f.lc_polynomial()
        lc_pol_inverted = [lc_pol[1], lc_pol[0]]

        m0 = Monomial(lc_pol_inverted, [0])
        p0 = Polynomial([m0])

        return f.multiply_polynomials(p0)

    def multivariable_division(self, array_polynomials):
        s = len(array_polynomials)
        var_max = 0
        for p in array_polynomials:
            for m in p.monomials:
                if len(m.m_exp) > var_max:
                    var_max = len(m.m_exp)
        p = Polynomial(var_max)
        array_u = [p] * s

        r = Polynomial(var_max)
        h = self
        h_empty = False

        while not h_empty:
            h.simplify()
            r.simplify()
            lp_h = h.lp_polynomial()
            lt_m = h.lt_polynomial()
            lt_p = Polynomial([lt_m])

            found = False
            i = 0
            while not found and i < len(array_polynomials):
                lp_f = array_polynomials[i].lp_polynomial()
                if lp_h.is_divisible(lp_f):
                    found = True
                else:
                    i += 1

            if found:
                lt_f = array_polynomials[i].lt_polynomial()
                division_sum_m = lt_m.division_monomials(lt_f)
                division_sub_m = lt_m.division_monomials(lt_f)

                division_sum_p = Polynomial([division_sum_m])
                division_sub_p = Polynomial([division_sub_m])
                array_u[i] = array_u[i].add_polynomial(division_sum_p)

                for monomial in division_sub_p.monomials:
                    monomial.coefficient[0] *= -1
                division_sub_p = division_sub_p.multiply_polynomials(
                    array_polynomials[i])
                h = h.add_polynomial(division_sub_p)
            else:
                r = r.add_polynomial(lt_p)
                _monomials = []
                for monomial in lt_p.monomials:
                    coef = [monomial.coefficient[0]
                            * -1, monomial.coefficient[1]]
                    m = Monomial(coef, monomial.m_exp)
                    _monomials.append(m)
                subtraction = Polynomial(_monomials)
                h = h.add_polynomial(subtraction)

            h_empty = True
            if h.monomials:
                for m in h.monomials:
                    for n in m.m_exp:
                        if n != 0:
                            h_empty = False
                    if m.coefficient[0] != 0:
                        h_empty = False

        array_u.append(r)
        return array_u

    def calculate_lcm_polynomials(self, p):
        m1 = self.lp_polynomial()
        m2 = p.lp_polynomial()

        exp_s_polynomial = []
        for i in range(len(m1.m_exp)):
            exp_s_polynomial.append(max(m1.m_exp[i], m2.m_exp[i]))

        unit = [1, 1]
        m_res = Monomial(unit, exp_s_polynomial)
        return m_res

    def calculate_s_polynomial(self, g):
        L = self.calculate_lcm_polynomials(g)
        lt_f = self.lt_polynomial()
        lt_g = g.lt_polynomial()

        division_f = L.division_monomials(lt_f)
        division_g = L.division_monomials(lt_g)
        division_g.coefficient[0] *= -1

        division_f_p = Polynomial([division_f])
        division_g_p = Polynomial([division_g])

        p_f = division_f_p.multiply_polynomials(self)
        p_g = division_g_p.multiply_polynomials(g)

        s = p_f.add_polynomial(p_g)
        return s.simplify()

    def calculate_grobner_bases(self, F):
        counter = 1
        G = F
        G_pairs = []
        for i in range(len(G)):
            for j in range(i + 1, len(G)):
                G_pairs.append([G[i], G[j]])

        while G_pairs:
            print()
            print("STEP", counter)

            print(len(G_pairs))
            counter += 1

            pair_removed = G_pairs.pop(0)

            pair_removed[0].simplify()
            pair_removed[1].simplify()

            S = pair_removed[0].calculate_s_polynomial(pair_removed[1])

            if S.monomials:
                S_division = S.multivariable_division(G)
                remainder = S_division[-1]

                if remainder.monomials:
                    # Verificar si el polinomio ya está en G
                    is_duplicate = False
                    for g in G:
                        if g.monomials == remainder.monomials:
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        G.append(remainder)
                        G_hash = set(G)
                        for g in G_hash:
                            if g != remainder:
                                G_pairs.append([g, remainder])

        return G

    def reduce_grobner(self, G):
        H = []
        R = []

        for p in G:
            copy = Polynomial(p.monomials)
            R.append(copy)

        for i in range(len(G)):
            g = Polynomial(G[i].monomials)
            R.pop(0)

            print()
            print("Iteration " + str(i))
            print("Removed polynomial:", g.read_polynomial())
            print()
            print("H:")
            for p in H:
                print(p.read_polynomial())

            print()
            print("R:")
            for p in R:
                print(p.read_polynomial())

            result_division = g.multivariable_division(R)
            remainder = result_division[-1]
            if remainder.monomials:
                print("Remainder:", remainder.read_polynomial())

                if not H and not R:  # Verificar si H y R están vacíos
                    return [Polynomial([Monomial([1, 1], [0])])]

                lc_double = remainder.lc_polynomial()
                for m in remainder.monomials:
                    monic = m.division_fraction(m.coefficient, lc_double)
                    m.coefficient[0] = monic[0]
                    m.coefficient[1] = monic[1]

                remainder.simplify()
                H.append(remainder)
                R.append(remainder)

        return H
