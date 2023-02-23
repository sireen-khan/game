my_character = Actor('square')
my_character.topright = 0, 10

WIDTH = 500
HEIGHT = my_character.height + 20

def draw():
    screen.clear()
    screen.fill((255,255,255))
    my_character.draw()

def update():
    my_character.left = my_character.left + 2
    if my_character.left > WIDTH:
        my_character.right = 0

def on_mouse_down(pos):
    if my_character.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
def on_mouse_down(pos):
    if my_character.collidepoint(pos):
        sounds.eep.play()
        my_character.image = 'char_w_hat'
def set_my_character_hurt():
    my_character.image = 'char_w_hat'
    sounds.eep.play()
    clock.schedule_unique(set_my_character_normal, 1.0)



