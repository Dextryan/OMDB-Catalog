class Movie(object):
    def __init__(self, json_data):
        # Função construtora, recebe um json e cria um objeto Movie
        self.title = json_data['Title']
        self.release_date = json_data['Released']
        self.rating = json_data['imdbRating']
        self.plot = json_data['Plot']
        self.director = json_data['Director']
        self.genre = json_data['Genre']

    def __str__(self):
        # Função que transforma o objeto em uma string
        return f"{self.title} ({self.release_date.split(' ')[2]}) - {self.rating}/10\nSinopse: {self.plot}\nGênero: {self.genre}\nDiretor: {self.director}"

    def __dict__(self):
        # Função que transforma o objeto em um dicionário, para ser armazenado em JSON
        return {
            "Title": self.title,
            "Released": self.release_date,
            "imdbRating": self.rating,
            "Plot": self.plot,
            "Director": self.director,
            "Genre": self.genre
        }
