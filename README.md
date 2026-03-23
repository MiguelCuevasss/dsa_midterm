# dsa_midterm

## Profiling de memoria

![Profiler Output](images/profiler_output.png)

DSA Midterm

Este proyecto implementa una playlist de musica usando una lista doblemente linkeada no circular, cada nodo es una cancion que tiene un nombre, un artista y un album.

La PLaylist tiene un play que reproduce la cancion actual, y un next que avanza a la siguiente cancion, al igual que un previous que regresa a la cancion anterior.

La playlist tiene un shuffle que puede activarse o desactivarse, no modifica la estructura original de la lista y puedes darle next y previous en modo shuffle.

Para activar el shuffle tiene una complejidad O(n) porque recorre todos los nodos o canciones, depende del tamaño de las canciones para hacer esto.

Para navegar siempre es O(1) porque siempre hace una instruccion independientemente de la cantidad de canciones, y para desactivar un shuffle siempre tiene un O(1) porque solo corre una instruccion.

El resultado del profiler dice que la mayor cantidad de ocurrencias pasa en el for, debido a que hace un loop de varias cosas, el incremento de la memoria es solo al inicio ya que crea un espacio en memoria para hacer esa funcion, el tiempo de carga es relativamente poco debido a que la cantidad de canciones no es tan significativa.

Como Clonar El Repo

    1. git clone (Tu link SSH)

Instalar dependencias

    pip install memory-profiler

Ejecutar el programa
    Python main.py

Ejecutar el profiling
    Python -m memory profler main.py    