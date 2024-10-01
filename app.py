import streamlit as st
import pandas as pd
import plotly.express as px

# Configurando o layout da página como "wide" para usar toda a largura da tela
st.set_page_config(layout="wide")

# Função para a Página 1
def pagina1():

    # Título da página 1
    st.title('Top-100 Trending Books')

    # Carregando os datasets de reviews e os 100 livros mais populares
    df_top100_books = pd.read_csv("Top-100 Trending Books.csv")

    df_reviews = pd.read_csv("customer reviews.csv")

    # Calculando os valores mínimo e máximo de preços dos livros
    price_max = df_top100_books["book price"].max()
    price_min = df_top100_books["book price"].min()

    # Slider na barra lateral para permitir ao usuário selecionar uma faixa de preço
    # O valor máximo inicial do slider é definido como o preço máximo dos livros
    max_price = st.sidebar.slider("Price Range", price_min,
                          price_max, price_max, format="$%f")

    # Filtrando o dataframe para exibir apenas os livros com preço abaixo do valor selecionado
    df_books = df_top100_books[df_top100_books["book price"] <= max_price]

    # Exibindo os dados filtrados em um dataframe interativo
    st.dataframe(df_books)

    # Criando dois gráficos com Plotly: um gráfico de barras para o ano de publicação
    # e um histograma para a distribuição de preços
    fig = px.bar(df_books["year of publication"].value_counts().sort_index())
    fig2 = px.histogram(df_books["book price"])

    # Criando duas colunas lado a lado para exibir os gráficos
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig)  # Exibindo o gráfico de barras na primeira coluna
    col2.plotly_chart(fig2)  # Exibindo o histograma de preços na segunda coluna

# Função para a Página 2
def pagina2():

    # Carregando os datasets de reviews e os 100 livros mais populares
    df_top100_books = pd.read_csv("Top-100 Trending Books.csv")

    df_reviews = pd.read_csv("customer reviews.csv")

    # Obtendo a lista de livros únicos para exibir no selectbox (caixa de seleção)
    books = df_top100_books["book title"].unique()

    # Selectbox na barra lateral para selecionar um livro
    book = st.sidebar.selectbox("Books", books)

    # Filtrando o dataframe dos livros e dos reviews para o livro selecionado
    df_book = df_top100_books[df_top100_books["book title"] == book]
    df_reviews_f = df_reviews[df_reviews["book name"] == book]

    # Extraindo as informações do livro selecionado para exibir na página
    book_title = df_book["book title"].iloc[0]  # Título do livro
    book_genre = df_book["genre"].iloc[0]  # Gênero do livro
    book_price = f"$ {df_book['book price'].iloc[0]}"  # Preço do livro formatado
    book_rating = df_book['rating'].iloc[0]  # Avaliação do livro
    book_year = df_book['year of publication'].iloc[0]  # Ano de publicação

    # Exibindo o título do livro como título da página
    st.title(book_title)
    # Exibindo o gênero do livro como subtítulo
    st.header(book_genre)

    # Criando três colunas para exibir informações sobre o preço, avaliação e ano de publicação
    col1, col2, col3 = st.columns([1, 1, 3])
    col1.metric("Price", book_price)  # Exibindo o preço
    col2.metric("Rating", book_rating)  # Exibindo a avaliação
    col3.metric("Year of Publication", book_year)  # Exibindo o ano de publicação

    # Adicionando um divisor para separar a seção de detalhes do livro dos reviews
    st.divider()

    # Exibindo as reviews para o livro selecionado
    # Iterando sobre as reviews e exibindo cada uma como uma mensagem de chat
    for row in df_reviews_f.values:
      message = st.chat_message(f"{row[4]}")  # Nome do usuário
      message.markdown(f"#### {row[2]}")  # Título da review
      message.write(row[5])  # Conteúdo da review

# Menu lateral para selecionar a página
st.sidebar.title('Navegação')
# Selectbox para escolher entre as duas páginas: 'Top-100 Trending Books' e 'Books Reviews'
pagina_selecionada = st.sidebar.selectbox('Selecione uma página', ['Top-100 Trending Books', 'Books Reviews'])

# Exibir a página selecionada
if pagina_selecionada == 'Top-100 Trending Books':
    pagina1()  # Carregar a função correspondente à página 1
elif pagina_selecionada == 'Books Reviews':
    pagina2()  # Carregar a função correspondente à página 2
