# TFGGrobnerJaime

Este repositorio contiene el código necesario para la computación de bases de Gröbner utilizando el algoritmo de Buchberger, así como para la computación de bases de Gröbner reducidas.

## Descripción

La teoría de Gröbner es una herramienta poderosa en álgebra computacional que proporciona métodos sistemáticos para resolver una amplia gama de problemas algebraicos. Este proyecto implementa algoritmos para calcular bases de Gröbner, fundamentales en el estudio de sistemas de ecuaciones polinomiales.

## Contenido

- `monomial.py`: Representa monomios y define métodos para operaciones básicas en monomios como suma, resta, multiplicación, división, etc. También define métodos para operaciones con fracciones y órdenes de términos.
- `polynomial.py`: Representa polinomios compuestos por monomios y define métodos para operaciones polinomiales como suma, resta, multiplicación, división, etc. También contiene métodos para simplificación de polinomios, encontrar términos principales, coeficientes principales y polinomios principales. Además, proporciona métodos para la división univariante y multivariable de polinomios usando el algoritmo de Euclides.
Es en este archivo donde se encuentran los algoritmos de Bucgberger y de cómputo de base de Gróbner reducida.
- `main.py`: Script principal que crea ejemplos de sistemas polinomiales y les aplica los algoritmos implementados.

## Licencia

Este proyecto cuenta con licencia conforme a los términos de la Licencia MIT.
