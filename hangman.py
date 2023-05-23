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

def draw_text(text, x, y, font):
    text_pic = font.render(text, True, BLACK)
    text_rect = text_pic.get_rect(center=(x, y))
    window.blit(text_pic, text_rect)

def random_word():
    words = ['cat', 'mouse', 'root', 'pterodactyl', 'river', 'string', 'spring', 'wine', 'aardvack', 'bean', 'dinosaur', 'kelp', 'sword', 'mathematics', 'ruler', 'glasses', 'imagination']
    guessed_word = choice(words).strip()
    return guessed_word

def hangman_update():
    try:
        window.blit(images[hangman_status], (0, 60))
    except:
        pass
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
    draw_text(display_word, 400+(450/2), 200, font1)
    hangman_update()
    draw_text('you tried:' + str(wrong_guesses), 450, 30, font1)
    #draw_text('games played: ' + str(games), 450, 480, font2)
    #draw_text('games won: ' + str(wins), 680, 480, font2)

def game_over():
    global finish
    global games
    global wins
    finish = True
    for letter in word:
        if not (letter in guesses):
            finish = False      
    if finish:
        draw_text("you win", 400+(450/2), 300, font1)
        draw_text('press SPACE to play again', 625, 360, font2)
        wins += 1
        games += 1
        
    if hangman_status == 10:
        draw_text("you lose", 400+(450/2), 250, font1)
        draw_text("the word was: " + word, 400+(450/2), 300, font1)
        draw_text('press SPACE to play again', 625, 360, font2)
        games += 1

font.init()
font1 = font.Font(None, 60)
font2 = font.Font(None, 45)

hangman_status = 0
guesses = []
wrong_guesses = []
run = True
finish = False
word = 'cat'

games = 0
wins = 0

while run:
    window_update()
    game_over()
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        if e.type == KEYDOWN:
            if e.key == K_SPACE and (hangman_status == 10 or finish):
                word = None
                reset()
            if e.key in range(K_a, K_z + 1) and not finish and hangman_status < 10:
                if e.unicode in guesses or e.unicode in wrong_guesses:
                    draw_text('Вы уже угадывали эту букву', 400+(450/2), 120, font2)
                elif e.unicode in word:
                    guesses += e.unicode
                    print(e.unicode)
                else:
                    wrong_guesses += e.unicode
                    print(wrong_guesses)
                    hangman_status += 1

    display.update()
    time.delay(60)