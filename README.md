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

[Pyngrok](https://pyngrok.readthedocs.io/en/latest/index.html#) - Para expor o servidor local (Streamlit) através de um túnel na web.

No Google Colab, você pode instalar essas bibliotecas executando o comando:

```!pip install streamlit pandas plotly pyngrok```

Além disso, é necessário o uso do ```ngrok``` para expor a aplicação no Google Colab, pois o Streamlit roda em localhost e precisa de um túnel para ser acessado na web.
## Google Colab

**1. Carregar os arquivos CSV:**

```customer reviews.csv```: Contém as avaliações (reviews) dos livros.

```Top-100 Trending Books.csv```: Contém os dados dos 100 livros mais populares (preço, ano de publicação, rating, etc.).

Você pode carregar esses arquivos no Google Colab usando a interface de upload ou adicionar seus caminhos diretamente no código.

**2. Escreva o código da aplicação no Colab:**

Copie e cole o código fornecido no arquivo app.py no Colab e execute:

```%%writefile app.py```

**3. Rodar o Streamlit:**
Para rodar a aplicação, utilize o seguinte comando no Colab:

```!streamlit run app.py &> /dev/null &```

**4. Conectar o ngrok:**

Abra o ngrok para acessar a aplicação no navegador:

```
from pyngrok import ngrok  
public_url = ngrok.connect(port='8501') 
print(public_url)
```

O link exibido (```public_url```) será a URL para acessar a aplicação rodando no Google Colab.
    
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

[Pyngrok](https://pyngrok.readthedocs.io/en/latest/index.html#) - Para expor o servidor local (Streamlit) através de um túnel na web.
## Melhorias

- Adicionar uma terceira página com mais estatísticas sobre as reviews (ex: análise de sentimentos).

- Implementar um sistema de busca por título de livro.

- Melhorar a interface para exibição de gráficos e reviews.

## Feedback

Se você tiver algum feedback, por favor me deixe saber por meio de laianne.cst27@gmail.com


## Licença

Este projeto é livre para uso, modificação e distribuição conforme a Licença do [MIT](https://choosealicense.com/licenses/mit/).


## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.


## Rodando localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  npm install
```

Inicie o servidor

```bash
  npm run start
```


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  npm run test
```

