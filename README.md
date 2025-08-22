# 🐍 Snake

### 📖 Description

Snake is a game where the player controls a snake on a grid. The snake can move in four directions: up, down, left, and right. The player can also grow the snake by eating food. The player loses if the snake hits the edge of the grid or itself.

### 📦 Structure

* Menu
* Map
* Movement



### 📚 Recordatorios

Trabajando en el menu, tengo que empezar a diseñar varios aspectos:
    · Primeramente, tengo que dividir el template del menu en una lista con cada una de las filas que componen el template.
    · A continuación, tengo que crear una funcion que imprima todas las filas, hasta encontrar una fila llena de =. En cuanto la encuentre, todas las filas que comprendan esa misma y la proxima fila de =, serán guardadas sus coordenadas en filas y columnas para poder utilizar luego una flecha para desplazarse por el menu.


Comenzando con el diseño del juego en si, teniendo ya practicamente acabados los menus:
    · Principalmente, nos encontraremos con unos 3 apartados principales: los objetos, la serpiente, y el propio mapa. Primeramente, se deberá empezar con la creación del modulo Map.py.
    · El módulo Map.py deberá imprimir un mapa en pantalla con un sistema de coordenadas suficientemente bueno como para acceder a él desde los modulos Snake.py o Object.py, y hacer que estos se muevan por el mapa simplemente devolviendo un cambio en la dirección de movimiento, y que el propio mapa gestione un movimiento continuo de la serpiente en un segundo thread dentro del archivo main.py.

        Es decir, lo primero es 