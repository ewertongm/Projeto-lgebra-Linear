"""
Módulo responsável por armazenar o corpus de treinamento e os casos de teste
para o classificador de notícias (Tecnologia vs. Futebol).
"""

# Conjunto de treinamento: 6 documentos balanceados (3 por categoria)
CORPUS_TREINO = [
    {
        "id": "Doc 1",
        "categoria": "Tecnologia",
        "texto": (
            "O avanço da inteligência artificial generativa transforma o "
            "desenvolvimento de software moderno. Engenheiros utilizam novos "
            "modelos neurais e algoritmos em nuvem para otimizar processos de "
            "programação, reduzindo o tempo de entrega e automatizando tarefas "
            "repetitivas nos sistemas computacionais corporativos."
        ),
    },
    {
        "id": "Doc 2",
        "categoria": "Tecnologia",
        "texto": (
            "A arquitetura de nuvem híbrida oferece escalabilidade e alta "
            "disponibilidade para o armazenamento seguro de grandes volumes de "
            "dados. Empresas modernas migram servidores locais para "
            "infraestruturas distribuídas com o objetivo de garantir segurança "
            "da informação e recuperação ágil de desastres operacionais."
        ),
    },
    {
        "id": "Doc 3",
        "categoria": "Tecnologia",
        "texto": (
            "Bancos de dados relacionais e sistemas gerenciadores processam "
            "transações simultâneas com consistência e integridade estrutural. "
            "O ajuste de índices e a otimização de consultas SQL elevam o "
            "desempenho das aplicações web, garantindo respostas rápidas aos "
            "usuários dos softwares conectados."
        ),
    },
    {
        "id": "Doc 4",
        "categoria": "Futebol",
        "texto": (
            "O atacante marcou dois gols decisivos na vitória emocionante da "
            "equipe durante a grande final do campeonato estadual. A torcida "
            "lotou o estádio coberto de bandeiras para comemorar o título "
            "invicto conquistado com excelente organização tática dentro do "
            "gramado."
        ),
    },
    {
        "id": "Doc 5",
        "categoria": "Futebol",
        "texto": (
            "O técnico promoveu mudanças estratégicas no meio de campo para "
            "reforçar a marcação e acelerar os contra-ataques pelas pontas "
            "laterais. Os jogadores mantiveram posse de bola constante, "
            "sufocando a defesa adversária e finalizando jogadas perigosas "
            "contra a trave do goleiro."
        ),
    },
    {
        "id": "Doc 6",
        "categoria": "Futebol",
        "texto": (
            "O árbitro apitou o término de uma disputa acirrada que terminou "
            "empatada após cobrança polêmica de pênalti no último minuto. O "
            "resultado manteve o clube na liderança isolada da tabela de "
            "classificação da liga nacional de futebol profissional."
        ),
    },
]

# Casos de teste obrigatórios (isolados do treinamento)
CASOS_TESTE = [
    {
        "id": "Teste 1",
        "categoria_esperada": "Tecnologia",
        "texto": (
            "O novo software corporativo armazena grandes volumes de dados em "
            "servidores distribuídos na nuvem, melhorando o desempenho dos "
            "sistemas e otimizando consultas estruturadas."
        ),
    },
    {
        "id": "Teste 2",
        "categoria_esperada": "Futebol",
        "texto": (
            "Os jogadores comemoraram a vitória no gramado após o atacante "
            "finalizar uma jogada perfeita e marcar o gol decisivo no "
            "campeonato da liga."
        ),
    },
]