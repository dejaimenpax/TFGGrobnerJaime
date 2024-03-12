class Monomial:
    def __init__(self, coefficient, m_exp):
        self.coefficient = coefficient
        self.m_exp = m_exp

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Monomial.gcd(b, a % b)

    def read_monomial(self):
        res = ""
        empty = True
        for i in self.m_exp:
            if i != 0:
                empty = False

        if self.coefficient[1] == 1:
            res = str(self.coefficient[0])
        else:
            res = str(self.coefficient[0]) + "/" + str(self.coefficient[1])

        if not empty:
            for i in range(len(self.m_exp)):
                if self.m_exp[i] != 0:
                    res += "x_" + str((i + 1))
                    if self.m_exp[i] > 1:
                        res += "^" + str(self.m_exp[i])

        return res

    def exp_sum(self):
        res = 0
        for exp in self.m_exp:
            res += exp
        return res

    def is_divisible(self, m):
        divisible = True

        for i in range(len(self.m_exp)):
            if self.m_exp[i] - m.m_exp[i] < 0:
                divisible = False
        return divisible

    ## OPERATIONS WITH FRACTIONS ##

    def sum_fraction(self, a, b):
        result = []

        numerator1 = a[0]
        denominator1 = a[1]

        numerator2 = b[0]
        denominator2 = b[1]

        den_new = denominator1 * denominator2
        num_new = (numerator1 * denominator2) + (numerator2 * denominator1)

        gcd = self.gcd(num_new, den_new)

        num_new //= gcd
        den_new //= gcd

        result.append(num_new)
        result.append(den_new)

        return result

    def subtract_fraction(self, a, b):
        result = []

        numerator1 = a[0]
        denominator1 = a[1]

        numerator2 = b[0]
        denominator2 = b[1]

        den_new = denominator1 * denominator2
        num_new = (numerator1 * denominator2) - (numerator2 * denominator1)

        gcd = self.gcd(num_new, den_new)

        num_new //= gcd
        den_new //= gcd

        result.append(num_new)
        result.append(den_new)

        return result

    def multiply_fraction(self, a, b):
        result = []

        numerator1 = a[0]
        denominator1 = a[1]

        numerator2 = b[0]
        denominator2 = b[1]

        num_new = numerator1 * numerator2
        den_new = denominator1 * denominator2

        gcd = self.gcd(num_new, den_new)

        num_new //= gcd
        den_new //= gcd

        result.append(num_new)
        result.append(den_new)

        return result

    def division_fraction(self, a, b):
        result = []

        numerator1 = a[0]
        denominator1 = a[1]

        numerator2 = b[0]
        denominator2 = b[1]

        num_new = numerator1 * denominator2
        den_new = denominator1 * numerator2

        gcd = self.gcd(num_new, den_new)

        num_new //= gcd
        den_new //= gcd

        result.append(num_new)
        result.append(den_new)

        return result

    ## OPERATIONS WITH MONOMIALS ##

    def sum_monomial(self, m):
        coef = self.sum_fraction(m.coefficient, self.coefficient)
        result = Monomial(coef, self.m_exp)
        return result

    def subtract_monimal(self, m):
        coef = self.subtract_fraction(m.coefficient, self.coefficient)
        result = Monomial(coef, self.m_exp)
        return result

    def division_monomials(self, m):
        coef = self.division_fraction(self.coefficient, m.coefficient)
        res_exp = [self.m_exp[i] - m.m_exp[i] for i in range(len(m.m_exp))]
        result = Monomial(coef, res_exp)
        return result

    def multiply_monomials(self, m):
        coef = self.multiply_fraction(self.coefficient, m.coefficient)
        res_exp = [self.m_exp[i] + m.m_exp[i] for i in range(len(m.m_exp))]
        result = Monomial(coef, res_exp)
        return result

    ## TERM ORDERS ##

    def deglex(self, m1):
        e1 = m1.exp_sum()
        e2 = self.exp_sum()
        if e1 > e2:
            return m1
        elif e2 > e1:
            return self
        else:
            for i in range(min(len(m1.m_exp), len(self.m_exp))):
                exp1 = m1.m_exp[i]
                exp2 = self.m_exp[i]
                if exp1 > exp2:
                    return m1
                elif exp2 > exp1:
                    return self
            return self

    def degrevlex(self, m1):
        e1 = m1.exp_sum()
        e2 = self.exp_sum()
        if e1 > e2:
            return m1
        elif e2 > e1:
            return self
        else:
            reversed_exp1 = m1.m_exp[::-1]
            reversed_exp2 = self.m_exp[::-1]
            for i in range(min(len(reversed_exp1), len(reversed_exp2))):
                exp1 = reversed_exp1[i]
                exp2 = reversed_exp2[i]
                if exp1 > exp2:
                    return m1
                elif exp2 > exp1:
                    return self
            return self

    def lex(self, m1):
        i = 0
        while i < len(m1.m_exp):
            if m1.m_exp[i] > self.m_exp[i]:
                return m1
            elif self.m_exp[i] > m1.m_exp[i]:
                return self
            i += 1
        return self
