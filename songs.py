def generate_songs() -> list[dict[str, str]]:
    base_songs = [
        ("Blinding Lights", "The Weeknd", "After Hours"),
        ("Shape of You", "Ed Sheeran", "Divide"),
        ("Levitating", "Dua Lipa", "Future Nostalgia"),
        ("Bad Guy", "Billie Eilish", "When We All Fall Asleep"),
        ("Peaches", "Justin Bieber", "Justice"),
        ("HUMBLE.", "Kendrick Lamar", "DAMN."),
        ("God's Plan", "Drake", "Scorpion"),
        ("Stay", "The Kid LAROI", "Stay"),
        ("As It Was", "Harry Styles", "Harry's House"),
        ("Sunflower", "Post Malone", "Hollywood's Bleeding"),
    ]

    songs = []

    # 🔁 Repetimos canciones reales hasta llegar a 100
    for i in range(100):
        name, artist, album = base_songs[i % len(base_songs)]

        songs.append(
            {
                "name": name,
                "artist": artist,
                "album": album,
            }
        )

    return songs