import requests
import movie
import json
import os


# Função para limpar o console
def clear():
    return os.system('cls')


def write_options():
    """Escrever as opções para o usuário
    """
    print("")
    print("O que deseja fazer?")
    print("1. Persquisar filme por nome")
    print("2. Adicionar o último filme pesquisado aos favoritos")
    print("3. Listar filmes favoritos")
    print("4. Sair")


def search_movie(movie_name):
    """Pesquisar filme por nome

    Args:
        movie_name (String): Nome do filme

    Returns:
        Objeto "Movie": Objeto contendo as informações do filme
    """
    url = f"http://www.omdbapi.com/?t={movie_name}&type=movie&apikey=fe59540c"
    response = requests.get(url)
    movie_data = response.json()
    return movie.Movie(movie_data)


def add_to_favorites(movie):
    """Adicionar filme aos favoritos

    Args:
        movie (Objeto "Movie"): Objeto contendo as informações do filme
    """

    dir_path = os.path.expanduser("~/Documents/FavoriteMovies")
    list_path = os.path.expanduser("~/Documents/FavoriteMovies/favorites.json")

    # Caso o caminho para o arquivo já exista, adiciona o filme à lista
    if (os.path.exists(list_path)):
        with open(list_path, "r") as f:
            favorites = json.load(f)
        favorites.append(movie.__dict__())
        with open(list_path, "w") as f:
            json.dump(favorites, f)
    # Caso o caminho para o arquivo não exista, cria a pasta, o arquivo e adiciona o filme à lista
    else:
        # Tratamento de erro para caso a pasta já exista mas o arquivo não
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            pass

        with open(list_path, "w") as f:
            favorites = [movie.__dict__()]
            json.dump(favorites, f)


def list_favorites():
    """Listar filmes favoritos
    """
    path = os.path.expanduser("~/Documents/FavoriteMovies/favorites.json")
    if (os.path.exists(path)):
        with open(path, "r") as f:
            favorites = json.load(f)
            for favorite in favorites:
                print(movie.Movie(favorite))
    else:
        print("Nenhum filme favorito")


def main():
    clear()
    movie = None
    # Loop principal, enquanto o usuário não digitar 4, o programa continua rodando
    while True:
        write_options()

        # Tratamento de erro para caso o usuário digite algo que não seja um número
        try:
            option = int(input("Digite a opção: "))
        except ValueError:
            print("Opção inválida!")
            continue

        if option == 1:
            clear()
            name = input("Digite o nome do filme: ")
            movie = search_movie(name)
            print(movie)
        elif option == 2:
            clear()
            if movie is None:
                print("Nenhum filme pesquisado")
            else:
                add_to_favorites(movie)
                print(f"{movie.title} adicionado aos favoritos")
                movie = None
        elif option == 3:
            clear()
            list_favorites()
            pass
        elif option == 4:
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
