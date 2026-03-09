# Bomberman IA

## Johanna Foston

## 22-SISN-2-036

## Descripcion
Juego estilo Bomberman desarrollado con Pygame. El jugador debe eliminar al enemigo usando bombas antes de que el enemigo lo atrape.

## Como Jugar
- Muévete con las flechas del teclado
- Presiona ESPACIO para colocar una bomba
- Las bombas explotan después de 3 segundos y destruyen bloques
- Elimina al enemigo con una bomba para ganar
- Si el enemigo te toca o te alcanza la explosión, pierdes
- Presiona ESCAPE para salir

## Inteligencia Artificial
- A*: El enemigo usa el algoritmo A* para encontrar el camino más corto hacia el jugador
- Árbol de Comportamiento: El enemigo decide si huir de bombas, perseguir al jugador o patrullar el mapa

## Cómo ejecutar
1. Instalar dependencias:
```
pip install -r requirements.txt
```
2. Ejecutar el juego desde la terminal:
```
py main.py
```

## Estructura del proyecto
proyecto/
├── main.py
├── scripts/
│   ├── astar.py
│   ├── behaviour_tree.py
│   ├── bomb.py
│   ├── enemy.py
│   ├── game.py
│   ├── map.py
│   ├── menu.py
│   ├── player.py
│   └── sonidos.py
├── assets/
│   ├── images/
│   ├── sounds/
│   └── music/
├── requirements.txt
└── README.md
## Video
[enlace al video de YouTube aquí]