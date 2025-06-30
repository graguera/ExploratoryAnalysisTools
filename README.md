# ExploratoryAnalysisTools
Ferramentas para Análise Exploratória de Dados: Conjunto de funções em Python para análise descritiva de bases de dados com variáveis categóricas e métricas, geração de relatórios em Markdown, e exportação para DOCX via Pandoc. Ideal para explorar relações entre variáveis e gerar insights estatísticos de forma prática e automatizada.

# Exploratory Data Analysis Tools

Ferramentas Python para análises exploratórias de dados, incluindo geração de relatórios em Markdown e conversão para DOCX.

## Funções Incluídas

### `explore_df`
Gera um relatório em Markdown com análise descritiva das variáveis de um DataFrame em relação a uma variável alvo categórica (binária ou com múltiplas categorias). Inclui testes de hipótese (qui-quadrado, t-test) e análise de multicolinearidade (VIF).

**Exemplo de uso:**
```python
report = explore_df(df, target='coluna_alvo')
```

### `markdown_to_docx`
Converte um relatório em Markdown para um arquivo DOCX usando Pandoc.

**Exemplo de uso:**
```python
markdown_to_docx(report, 'saida.docx')
```

## Requisitos

- Python 3.7+
- pacotes em `requirements.txt`
- [Pandoc](https://pandoc.org) instalado no sistema

## Licença

MIT License
