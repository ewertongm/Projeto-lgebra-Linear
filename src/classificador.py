"""
Módulo do classificador supervisionado por centróides e similaridade de cossenos.
"""

from algebra_linear import soma_vetores, divide_escalar, similaridade_cosseno
from tfidf import vetorizar_texto_teste


def calcular_centroides(documentos_treino, vetores_treino, dimensao):
    """
    Calcula o vetor centróide (média vetorial) para cada categoria presente
    no conjunto de treinamento.
    """
    somas_por_classe = {}
    contagem_por_classe = {}

    for i, doc in enumerate(documentos_treino):
        categoria = doc["categoria"]
        vetor = vetores_treino[i]

        if categoria not in somas_por_classe:
            somas_por_classe[categoria] = [0.0] * dimensao
            contagem_por_classe[categoria] = 0

        somas_por_classe[categoria] = soma_vetores(somas_por_classe[categoria], vetor)
        contagem_por_classe[categoria] += 1

    centroides = {}
    for categoria, soma_vetorial in somas_por_classe.items():
        centroides[categoria] = divide_escalar(
            soma_vetorial, contagem_por_classe[categoria]
        )

    return centroides


def classificar_texto(texto, vocabulario, vetor_idf, centroides):
    """
    Vetoriza um novo texto, calcula a similaridade de cossenos com cada centróide
    e retorna a categoria vencedora, os índices obtidos e o vetor gerado.
    """
    vetor_teste = vetorizar_texto_teste(texto, vocabulario, vetor_idf)
    similaridades = {}

    for categoria, vetor_centroide in centroides.items():
        similaridades[categoria] = similaridade_cosseno(vetor_teste, vetor_centroide)

    maior_similaridade = max(similaridades.values())
    if maior_similaridade == 0.0:
        return "Indefinido (termos fora do vocabulário)", similaridades, vetor_teste

    categoria_vencedora = max(similaridades, key=similaridades.get)
    return categoria_vencedora, similaridades, vetor_teste