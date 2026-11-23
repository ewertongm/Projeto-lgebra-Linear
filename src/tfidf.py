"""
Módulo responsável pela ponderação TF-IDF e representação vetorial de documentos.
"""

import math
from preprocessamento import preprocessar_documento


def calcular_tf(tokens_documento, vocabulario):
    """
    Calcula a frequência relativa (TF) de cada termo do vocabulário
    dentro de um documento tokenizado.
    """
    total_palavras = len(tokens_documento)
    vetor_tf = []

    for termo in vocabulario:
        if total_palavras == 0:
            vetor_tf.append(0.0)
        else:
            ocorrencias = tokens_documento.count(termo)
            vetor_tf.append(ocorrencias / total_palavras)

    return vetor_tf


def calcular_idf(lista_tokens_documentos, vocabulario):
    """
    Calcula o Inverse Document Frequency (IDF) de cada termo do vocabulário:
    IDF(t) = ln(N / df_t)
    """
    total_docs = len(lista_tokens_documentos)
    vetor_idf = []

    for termo in vocabulario:
        docs_com_termo = 0
        for tokens in lista_tokens_documentos:
            if termo in tokens:
                docs_com_termo += 1

        if docs_com_termo > 0:
            vetor_idf.append(math.log(total_docs / docs_com_termo))
        else:
            vetor_idf.append(0.0)

    return vetor_idf


def gerar_matriz_tfidf(documentos_treino, vocabulario):
    """
    Constrói os vetores TF-IDF para todos os documentos de treinamento
    e retorna também o vetor IDF global para uso na classificação.
    """
    lista_tokens = [preprocessar_documento(doc["texto"]) for doc in documentos_treino]
    vetor_idf = calcular_idf(lista_tokens, vocabulario)
    vetores_documentos = []

    for tokens in lista_tokens:
        vetor_tf = calcular_tf(tokens, vocabulario)
        vetor_tfidf = [vetor_tf[i] * vetor_idf[i] for i in range(len(vocabulario))]
        vetores_documentos.append(vetor_tfidf)

    return vetores_documentos, vetor_idf


def vetorizar_texto_teste(texto, vocabulario, vetor_idf):
    """
    Projeta um texto inédito no espaço vetorial R^n utilizando o vocabulário
    e os pesos IDF congelados no treinamento.
    """
    tokens = preprocessar_documento(texto)
    vetor_tf = calcular_tf(tokens, vocabulario)
    return [vetor_tf[i] * vetor_idf[i] for i in range(len(vocabulario))]