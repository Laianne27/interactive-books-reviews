# interactive-books-reviews

Projeto: Top-100 Trending Books e Reviews

Este projeto utiliza o Streamlit para criar uma aplicação web interativa que exibe informações sobre os 100 livros mais populares e permite a visualização de suas avaliações (reviews) por parte dos leitores. A aplicação é dividida em duas páginas principais: uma para explorar os livros mais populares e outra para visualizar os detalhes e reviews de cada livro individualmente.
## Funcionalidades

**1. Top-100 Trending Books**

Exibe uma lista dos 100 livros mais populares, permitindo que os usuários filtrem por faixa de preço. Apresenta dois gráficos:

- Distribuição dos anos de publicação dos livros em um gráfico de barras.
- Histograma de preços dos livros.

A tabela de livros é interativa e reflete o filtro de preços selecionado, ajudando a explorar os livros dentro de um orçamento específico.

**2. Books Reviews**

Permite selecionar um livro específico para visualizar suas informações detalhadas, como:
- Gênero
 - Preço
 - Avaliação (rating)
- Ano de publicação
 
Exibe as avaliações (reviews) dos leitores para o livro selecionado, incluindo:
- Nome do usuário que fez a review
- Título da review
- Conteúdo da review
 
As reviews são apresentadas em formato de mensagens, tornando a visualização mais interativa e visualmente agradável.

## Instalação

Antes de rodar o projeto, você precisará instalar as seguintes bibliotecas:

[Streamlit](https://docs.streamlit.io/) - Para criar interfaces web interativas.

[Pandas](https://pandas.pydata.org/docs/) - Para manipulação e análise de dados.

[Plotly](https://plotly.com/graphing-libraries/)  - Para visualizações interativas e gráficos.

No Google Colab, você pode instalar essas bibliotecas executando o comando:

```!pip install streamlit pandas plotly```

Para rodar o projeto localmente no VS Code, você precisará ter o Python instalado e utilizar o terminal integrado para instalar as bibliotecas via pip. Siga os passos abaixo:

1. Abra o VS Code e navegue até o seu projeto.

2. Abra o terminal integrado no VS Code:
- No menu superior, vá em Terminal > New Terminal.
3. Instale as bibliotecas necessárias com o comando abaixo no terminal:
```pip install streamlit pandas plotly```

4. Rodar a aplicação:

- Para iniciar o Streamlit e rodar sua aplicação, execute o seguinte comando no terminal do VS Code:
```streamlit run app.py```

Isso abrirá a aplicação no navegador padrão. O Streamlit rodará localmente na porta 8501 (http://localhost:8501).

Além disso, a aplicação está hospedada no Render, através do link https://interactive-books-reviews.onrender.com/ facilitando o acesso a partir de qualquer navegador sem a necessidade de rodar localmente. O Render oferece um serviço de hospedagem de aplicações web, garantindo que o projeto esteja sempre acessível na web, sem a necessidade de configurações extras de túnel ou servidor local.
## Estrutura

```bash
├── app.py                  # Código principal da aplicação Streamlit
├── customer reviews.csv     # Arquivo CSV contendo as avaliações (reviews) dos livros
├── Top-100 Trending Books.csv  # Arquivo CSV contendo os dados dos 100 livros mais populares
└── README.md                # Arquivo de documentação do projeto
```

### Explicação do Código Principal (app.py)

O código da aplicação ```app.py``` é dividido em duas páginas principais:

**Função ```pagina1()``` (Top-100 Trending Books):**

- Carrega os dados de reviews e os dados dos 100 livros mais populares.
- Permite ao usuário filtrar os livros por uma faixa de preço.
- Exibe os livros que correspondem ao filtro selecionado e gera dois gráficos interativos: um gráfico de barras para o ano de publicação dos livros e um histograma para a distribuição de preços.

**Função ```pagina2()``` (Books Reviews):**

- Permite ao usuário selecionar um livro específico através de uma caixa de seleção (selectbox).
- Exibe os detalhes do livro selecionado, como preço, avaliação e ano de publicação.
- Mostra as avaliações (reviews) feitas pelos leitores do livro escolhido, utilizando um formato de mensagem de chat.

A navegação entre as duas páginas é feita através de um menu lateral (sidebar) utilizando a função ```st.sidebar.selectbox()```.
## Documentação

[Streamlit](https://docs.streamlit.io/) - Para criar interfaces web interativas.

[Pandas](https://pandas.pydata.org/docs/) - Para manipulação e análise de dados.


[Plotly](https://plotly.com/graphing-libraries/)  - Para visualizações interativas e gráficos.

## Melhorias

- Adicionar uma terceira página com mais estatísticas sobre as reviews (ex: análise de sentimentos).

- Implementar um sistema de busca por título de livro.

- Melhorar a interface para exibição de gráficos e reviews.

## Feedback

Se você tiver algum feedback, por favor me deixe saber por meio de laianne.cst27@gmail.com


## Licença

Este projeto é livre para uso, modificação e distribuição conforme a Licença do [MIT](https://choosealicense.com/licenses/mit/).

