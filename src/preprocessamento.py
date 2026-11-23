"""
Módulo de pré-processamento textual e construção do vocabulário base
que define os eixos dimensionais do espaço vetorial R^n.
"""

STOPWORDS = {
    "a", "as", "o", "os", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "em", "no", "na",
    "nos", "nas", "por", "pelo", "pela", "pelos", "pelas",
    "para", "com", "sem", "sob", "sobre", "entre", "até",
    "e", "ou", "mas", "pois", "que", "se", "como", "ao", "aos"
}


def limpar_texto(texto):
    """Converte o texto para minúsculas e substitui pontuações por espaços."""
    texto_minusculo = texto.lower()
    caracteres_validos = []

    for caractere in texto_minusculo:
        if caractere.isalpha() or caractere.isspace():
            caracteres_validos.append(caractere)
        else:
            caracteres_validos.append(" ")

    return "".join(caracteres_validos)


def tokenizar(texto_limpo):
    """Divide uma string limpa em uma lista de palavras individuais (tokens)."""
    return texto_limpo.split()


def remover_stopwords(tokens):
    """Remove stopwords e tokens de apenas um caractere."""
    tokens_filtrados = []
    for palavra in tokens:
        if palavra not in STOPWORDS and len(palavra) > 1:
            tokens_filtrados.append(palavra)
    return tokens_filtrados


def preprocessar_documento(texto):
    """Executa limpeza, tokenização e filtragem de stopwords em um texto."""
    texto_limpo = limpar_texto(texto)
    tokens = tokenizar(texto_limpo)
    return remover_stopwords(tokens)


def construir_vocabulario(documentos_treino):
    """
    Extrai e ordena alfabeticamente os termos únicos do corpus de treino,
    definindo a base canônica do espaço R^n.
    """
    termos_unicos = set()
    for doc in documentos_treino:
        tokens = preprocessar_documento(doc["texto"])
        for termo in tokens:
            termos_unicos.add(termo)

    return sorted(list(termos_unicos))