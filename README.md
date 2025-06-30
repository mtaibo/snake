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