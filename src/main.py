"""
Ponto de entrada da aplicação: executa o treinamento, roda os 2 casos de teste
obrigatórios do relatório e permite a classificação interativa de novos textos.
"""

from dataset import CORPUS_TREINO, CASOS_TESTE
from preprocessamento import construir_vocabulario
from tfidf import gerar_matriz_tfidf
from classificador import calcular_centroides, classificar_texto


def exibir_coordenadas_ativas(vetor, vocabulario):
    """Exibe apenas os termos com peso > 0 para facilitar a leitura no terminal."""
    ativos = []
    for i, peso in enumerate(vetor):
        if peso > 0:
            ativos.append(f"{vocabulario[i]}: {peso:.4f}")
    return ", ".join(ativos)


def main():
    print("=" * 70)
    print("CLASSIFICADOR DE TEXTOS POR ESPAÇO VETORIAL (TF-IDF + COSSENO)")
    print("=" * 70)

    # 1. Fase de Treinamento
    vocabulario = construir_vocabulario(CORPUS_TREINO)
    vetores_treino, vetor_idf = gerar_matriz_tfidf(CORPUS_TREINO, vocabulario)
    centroides = calcular_centroides(CORPUS_TREINO, vetores_treino, len(vocabulario))

    print(f"\n[TREINAMENTO CONCLUÍDO]")
    print(f"Documentos de treino: {len(CORPUS_TREINO)}")
    print(f"Dimensão do espaço vetorial (R^n): n = {len(vocabulario)} termos únicos")
    print(f"Categorias modeladas: {list(centroides.keys())}\n")

    # 2. Execução dos 2 Casos de Teste Obrigatórios
    print("-" * 70)
    print("EXECUÇÃO DOS CASOS DE TESTE OBRIGATÓRIOS")
    print("-" * 70)

    for teste in CASOS_TESTE:
        categoria_predita, sims, vetor_teste = classificar_texto(
            teste["texto"], vocabulario, vetor_idf, centroides
        )
        vetor_arredondado = [round(v, 4) for v in vetor_teste]

        print(f"\n>>> {teste['id']} (Esperado: {teste['categoria_esperada']})")
        print(f"Entrada: \"{teste['texto']}\"")
        print(f"Termos ativados no vocabulário: [{exibir_coordenadas_ativas(vetor_teste, vocabulario)}]")
        print(f"Vetor completo (R^{len(vocabulario)}): {vetor_arredondado}")
        for cat, valor in sims.items():
            print(f"  - Similaridade com Centróide {cat}: {valor:.4f}")
        print(f"Classificação Obtida: {categoria_predita}")

    # 3. Modo interativo para testes adicionais do usuário
    print("\n" + "-" * 70)
    print("MODO INTERATIVO (Digite 'sair' para encerrar)")
    print("-" * 70)

    while True:
        entrada = input("\nDigite um texto de notícia para classificar: ").strip()
        if entrada.lower() == "sair":
            break
        if not entrada:
            continue

        categoria_predita, sims, vetor_teste = classificar_texto(
            entrada, vocabulario, vetor_idf, centroides
        )
        print(f"Termos reconhecidos: [{exibir_coordenadas_ativas(vetor_teste, vocabulario)}]")
        for cat, valor in sims.items():
            print(f"  - Similaridade com Centróide {cat}: {valor:.4f}")
        print(f"Categoria Atribuída: {categoria_predita}")


if __name__ == "__main__":
    main()