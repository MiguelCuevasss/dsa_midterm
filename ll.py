from __future__ import annotations
from memory_profiler import profile
import time
import random

class Node:
    def __init__(self, name: str, artist: str, album: str) -> None:
        self.name: str = name
        self.artist: str = artist
        self.album: str = album

        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self) -> str:
        return f"{self.name} - {self.artist} ({self.album})"


class Playlist:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.current: Node | None = None
        self.size: int = 0

        self.shuffle_on = False
        self.shuffle_forward: dict[Node, Node | None] = {}
        self.suffle_backward: dict[Node, Node | None] = {}

    def append(self, name: str, artist: str, album: str) -> None:
        new_node = Node(name, artist, album)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def play(self) -> str:
        if self.current is None:
            return "La playlist está vacía."
        return f"Reproduciendo: {self.current}"

    def next(self) -> str:
        if self.current is None:
            return "La playlist está vacía."

        if self.current.next is None:
            return "Ya estás en la última canción."

        self.current = self.current.next
        return f"Reproduciendo: {self.current}"

    def previous(self) -> str:
        if self.current is None:
            return "La playlist está vacía."

        if self.current.prev is None:
            return "Ya estás en la primera canción."

        self.current = self.current.prev
        return f"Reproduciendo: {self.current}"

    def print_playlist(self) -> None:
        current = self.head

        while current is not None:
            marker = " <-- current" if current == self.current else ""
            print(current, marker)
            current = current.next

    @profile
    def load_songs(self, songs: list[dict[str, str]]) -> float:
        start_time = time.perf_counter()

        for song in songs:
            self.append(song["name"], song["artist"], song["album"])

        end_time = time.perf_counter()
        return end_time - start_time
    
    def _get_nodes(self) -> list[Node]:
        nodes = []
        current = self.head

        while current is not None:
            nodes.append(current)
            current = current.next

        return nodes

    def enable_shuffle(self) -> None:

        nodes = self._get_nodes()

        if len(nodes) <= 1:
            return

        shuffled = nodes[:]
        random.shuffle(shuffled)

        self.shuffle_forward.clear()
        self.shuffle_backward.clear()

        for i in range(len(shuffled) - 1):
            self.shuffle_forward[shuffled[i]] = shuffled[i + 1]
            self.shuffle_backward[shuffled[i + 1]] = shuffled[i]

        self.shuffle_forward[shuffled[-1]] = None
        self.shuffle_backward[shuffled[0]] = None

        self.shuffle_on = True

        if self.current is None:
            self.current = shuffled[0]

    def disable_shuffle(self) -> None:
        self.shuffle_on = False
        self.shuffle_forward.clear()
        self.shuffle_backward.clear()