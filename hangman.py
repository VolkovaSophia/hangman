from pygame import *
from random import *

width = 900
height = 500
window = display.set_mode((width, height))
display.set_caption('HANGMAN')
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
window.fill(WHITE)

images = []
for i in range(11):
    pic = image.load('hangman'+str(i)+'.png')
    images.append(pic)

def draw_text(text, x, y):
    text_pic = font.render(text, True, BLACK)
    window.blit(text_pic, (x, y))

def random_word():
    the = ['cat', 'mouse', 'rats', 'wellhellothere']
    guessed_word = choice(the).strip()
    return guessed_word

def hangman_update():
    window.blit(images[hangman_status], (0, 60))
    display.update()

def reset():
    global hangman_status
    global guesses
    global word
    global wrong_guesses

    hangman_status = 0
    guesses = []
    wrong_guesses = []
    word = random_word()

def window_update():
    window.fill(WHITE)
    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter + ' '
        else:
            display_word += '_ '
    draw_text(display_word, 400, 200)
    hangman_update()
    draw_text('you tried:' + str(wrong_guesses), 10, 10)

def game_over():
    finish = True
    for letter in word:
        if not (letter in guesses):
            finish = False      
    if finish:
        draw_text("you win", 520, 300)
        draw_text('press SPACE to play again', 340, 350)

    if hangman_status == 10:
        draw_text("you lose", 520, 300)
        draw_text('press SPACE to play again', 340, 350)
    


font.init()
font = font.Font(None, 60)

hangman_status = 0
guesses = []
wrong_guesses = []
run = True
finish = False
word = 'cat'


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                word = None
                reset()
            if e.key in range(K_a, K_z + 1):
                if e.unicode in guesses or e.unicode in wrong_guesses:
                    pass
                elif e.unicode in word:
                    guesses += e.unicode
                    print(e.unicode)
                else:
                    wrong_guesses += e.unicode
                    print(wrong_guesses)
                    hangman_status += 1
    window_update()
    game_over()
    display.update()
    time.delay(60)