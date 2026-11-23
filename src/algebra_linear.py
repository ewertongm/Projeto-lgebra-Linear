"""
Módulo de operações primitivas de Álgebra Linear em R^n.
Implementado manualmente utilizando apenas listas nativas e math.sqrt.
"""

import math


def produto_escalar(vetor_a, vetor_b):
    """Calcula o produto interno usual <u, v> = soma(u_i * v_i)."""
    if len(vetor_a) != len(vetor_b):
        raise ValueError("Os vetores devem possuir a mesma dimensão.")

    soma = 0.0
    for i in range(len(vetor_a)):
        soma += vetor_a[i] * vetor_b[i]
    return soma


def norma_vetorial(vetor):
    """Calcula a norma euclidiana ||v|| = sqrt(soma(v_i^2))."""
    soma_quadrados = 0.0
    for componente in vetor:
        soma_quadrados += componente ** 2
    return math.sqrt(soma_quadrados)


def soma_vetores(vetor_a, vetor_b):
    """Realiza a adição componente a componente entre dois vetores em R^n."""
    if len(vetor_a) != len(vetor_b):
        raise ValueError("Os vetores devem possuir a mesma dimensão.")

    resultado = []
    for i in range(len(vetor_a)):
        resultado.append(vetor_a[i] + vetor_b[i])
    return resultado


def divide_escalar(vetor, escalar):
    """Divide cada componente de um vetor por um escalar não nulo."""
    if escalar == 0:
        raise ValueError("Divisão por zero não permitida.")

    resultado = []
    for componente in vetor:
        resultado.append(componente / escalar)
    return resultado


def similaridade_cosseno(vetor_a, vetor_b):
    """
    Calcula o cosseno do ângulo entre dois vetores:
    cos(theta) = (u . v) / (||u|| * ||v||)
    """
    norma_a = norma_vetorial(vetor_a)
    norma_b = norma_vetorial(vetor_b)

    # Evita divisão por zero caso um texto de teste não tenha palavras no vocabulário
    if norma_a == 0.0 or norma_b == 0.0:
        return 0.0

    prod_interno = produto_escalar(vetor_a, vetor_b)
    return prod_interno / (norma_a * norma_b)