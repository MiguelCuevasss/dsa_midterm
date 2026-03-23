def generate_songs() -> list[dict[str, str]]:
    songs = []

    for i in range(1, 101):
        songs.append(
            {
                "name": f"Song {i}",
                "artist": f"Artist {((i - 1) % 10) + 1}",
                "album": f"Album {((i - 1) % 5) + 1}",
            }
        )

    return songs