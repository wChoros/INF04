class Song:
    def __init__(
        self,
        author: str = None,
        name: str = None,
        number_of_tracks: int = None,
        year: int = None,
        downloads: int = None,
    ):
        self.author = author
        self.name = name
        self.number_of_tracks = number_of_tracks
        self.year = year
        self.downloads = downloads

    def __str__(self):
        return f"""
{self.author}
{self.name}
{self.number_of_tracks}
{self.year}
{self.downloads}
"""


# **********************************************
# nazwa funkcji: load_songs
# opis funkcji: ładuje dane piosenek z pliku
# parametry: brak
# zwracany typ i opis: list[Song] - Lista obiektów klasy Song
# autor: 00000000000
# ***********************************************
def load_songs() -> list[Song]:
    songs = []
    with open("data/Data.txt") as file:
        line = file.readline().strip()
        while line:
            song = Song()
            song.author = line
            song.name = file.readline().strip()
            song.number_of_tracks = file.readline().strip()
            song.year = file.readline().strip()
            song.downloads = int(file.readline().strip())

            songs.append(song)

            line = file.readline()
            line = file.readline().strip()
    return songs


def print_songs(songs):
    for song in songs:
        print(song)


if __name__ == "__main__":
    songs = load_songs()
    print_songs(songs)
