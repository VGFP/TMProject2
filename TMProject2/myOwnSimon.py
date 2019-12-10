
from random import choice
from time import sleep
from turtle import *
pattern = []
guesses = []
from freegames import floor, square, vector
import time

pattern = []
guesses = []
tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}

def grid():
    "Draw grid of tiles."
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()

def flash(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.5)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.5)

def grow():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def tap(x,y):
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        print("Wrong")
        #exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

def start():
    "Start game."
    grow()
    print("I am in start")

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
print("I am in main script 1")
gameStarted=True
i=0
while(gameStarted):
    start()
    #here add voice controll as async function
    time.sleep(2)

    print("I am in main script 2")
done()
