# Write your code here :-)
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
fox = Actor("character")
fox.pos = 100, 100

coin = Actor("square")
coin.pos = 200,200

def draw():
    screen.fill("green")
    character.draw()
    square.draw()
    screen.draw.text("Score: " +
