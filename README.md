# OMDB-Catalog

Aplicação em python para pesquisar e favoritar filmes usando a API OMDB

O programa conta com as seguintes opções:

1. Pesquisar filme por nome;
   - A busca retorna o nome, o ano de lançamento, a classificação IMDB, a sinopse, o genero e o diretor do filme
2. Favoritar filmes
   - Os filmes favoritos ficam salvos em um arquivo JSON na pasta FavoriteMovies, dentro da pasta Documentos
3. Ver a listagem dos filmes favoritos
4. Remover seletivamente um filme dos filmes favorito

Para fazer a busca na OMDB API, usa-se uma chave de API única para cada desenvolvedor. Para fins avaliativos, a chave foi deixada dentro do código, entretanto é importante notar que em uma aplicação comercial, a chave jamais deve ficar exposta.
