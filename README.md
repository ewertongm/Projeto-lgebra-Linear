


# Classificador de Textos por Espaço Vetorial (TF-IDF + Similaridade de Cossenos)

Sistema de classificação supervisionada de notícias em **Tecnologia** e **Futebol** fundamentado no modelo de espaço vetorial ($\mathbb{R}^n$), desenvolvido em **Python 3.14.2** utilizando apenas estruturas nativas da linguagem e funções algébricas primitivas (sem bibliotecas externas de aprendizado de máquina ou álgebra linear).

Projeto desenvolvido como requisito parcial da disciplina **SPOMVAL – Vetores, Geometria Analítica e Álgebra Linear**, do curso de Bacharelado em Sistemas de Informação do **Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP – Campus São Paulo)**.

---

## Autores e Orientação

* **Dennis Daigo Olher**
* **Ewerton Godinho Monteiro**
* **Thúlio Souza Alves**
* **Orientação:** Prof.ª Dr.ª Josceli Maria Tenorio

---

## Estrutura do Repositório

```text
classificador-texto-espaco-vetorial/
├── docs/
│   └── Relatorio_Algebra_Linear_Tema5.pdf
├── src/
│   ├── __init__.py
│   ├── dataset.py
│   ├── preprocessamento.py
│   ├── algebra_linear.py
│   ├── tfidf.py
│   ├── classificador.py
│   └── main.py
├── .gitignore
└── README.md

```

### Descrição dos Módulos

* **`src/dataset.py`**: Armazena o *corpus* rotulado de treinamento (6 documentos balanceados: 3 de *Tecnologia* e 3 de *Futebol*) e os 2 casos de teste inéditos para validação.
* **`src/preprocessamento.py`**: Realiza a normalização textual (conversão para minúsculas, remoção de pontuações e filtragem de *stopwords*) e constrói o vocabulário base ordenado alfabeticamente ($n = 154$ dimensões).
* **`src/algebra_linear.py`**: Implementa manualmente as rotinas matemáticas primitivas em $\mathbb{R}^n$: produto interno (`produto_escalar`), norma euclidiana (`norma_vetorial`), soma de vetores (`soma_vetores`), divisão por escalar (`divide_escalar`) e similaridade de cossenos (`similaridade_cosseno`).
* **`src/tfidf.py`**: Calcula a frequência relativa dos termos (`calcular_tf`), a frequência inversa no acervo (`calcular_idf`), a matriz termo-documento de treino e a vetorização de novas entradas.
* **`src/classificador.py`**: Calcula os vetores centróides (média vetorial) de cada editoria e realiza a classificação de novos textos pela maior similaridade angular ($\cos\theta$).
* **`src/main.py`**: Orquestra o treinamento, executa automaticamente os dois casos de teste obrigatórios e disponibiliza um modo interativo no terminal.
* **`docs/Relatorio_Algebra_Linear_Tema5.pdf`**: Relatório técnico completo contendo fundamentação teórica, modelagem, código comentado e análise dos resultados.

---

## Fundamentos Matemáticos Implementados

1. **Espaço Vetorial ($\mathbb{R}^{154}$):** Cada termo único extraído do *corpus* de treinamento define um eixo da base canônica.
2. **Ponderação TF-IDF:**

$$w_{i,j} = \text{TF}(t_i, d_j) \cdot \ln\left(\frac{N}{df_i}\right)$$


3. **Vetores Centróides:** Média vetorial (combinação linear com escalares $1/k$) dos documentos pertencentes à mesma categoria:

$$\vec{\mu}_m = \frac{1}{k}\sum_{j=1}^{k} \vec{d}_j$$


4. **Similaridade de Cossenos:** Mede o alinhamento angular entre o vetor de teste $\vec{x}$ e cada centróide $\vec{\mu}_m$:

$$\cos(\theta) = \frac{\vec{x} \cdot \vec{\mu}_m}{\|\vec{x}\| \cdot \|\vec{\mu}_m\|}$$



---

## Pré-requisitos e Execução

* **Python 3.10+** (desenvolvido e testado na versão **3.14.2**).
* Nenhuma dependência externa é necessária (utiliza apenas estruturas nativas e o módulo padrão `math`).

Para executar o projeto a partir da raiz do repositório:

```bash
# Windows (via launcher py)
py src/main.py

# Linux / macOS / Windows (com python no PATH)
python src/main.py

```

### Exemplo de Saída Esperada (Casos de Teste Obrigatórios)

* **Caso de Teste 1 (Tecnologia):** $\cos(\theta_{\text{Tecnologia}}) = 0{,}3490$ | $\cos(\theta_{\text{Futebol}}) = 0{,}0000$ $\rightarrow$ **Tecnologia**
* **Caso de Teste 2 (Futebol):** $\cos(\theta_{\text{Tecnologia}}) = 0{,}0000$ | $\cos(\theta_{\text{Futebol}}) = 0{,}2948$ $\rightarrow$ **Futebol**
