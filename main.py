from ll import Playlist
from songs import generate_songs


def main() -> None:
    playlist = Playlist()

    songs = generate_songs()

    elapsed_time = playlist.load_songs(songs)

    print(f"Tiempo de carga: {elapsed_time:.8f} segundos")
    print(f"Total de canciones: {playlist.size}")
    print()

    print(playlist.play())      
    print(playlist.next())      
    print(playlist.next())      
    print(playlist.previous())  


if __name__ == "__main__":
    main()