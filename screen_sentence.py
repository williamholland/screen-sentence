import re
import sys
import pygame
import nltk
import logging

import word_class

logging.basicConfig(format='%(asctime)s File %(name)s, line %(lineno)d, %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

pygame.init()

infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
BLACK = 0,0,0
WHITE = 255,255,255
screen.fill(WHITE)


def word_colour(word):
    ''' given a word, find the colour for syntax hilighting '''

    tag = nltk.pos_tag([word])[0]

    logger.info(tag)

    return word_class.TAGS.get(tag[1], word_class.DEFAULT).colour


def exit(event):
    logger.info('exit')
    sys.exit()


def noop(*args, **kwargs):
    pass

def get_font(text):
    ''' (str,) -> (position, font)
    
        get the font, find the fontsize that will fill the screen
        get the position that will centre this text on the screen
    '''
    infoObject = pygame.display.Info()
    screen_w, screen_h = infoObject.current_w, infoObject.current_h
    test_font = pygame.font.SysFont("LiberationSans", 10)
    ratio = (test_font.size(TEXT)[0] / float(len(TEXT))) / 10.0
    font_size = int(round(min((screen_w/ratio) / len(TEXT), screen_h )))
    font = pygame.font.SysFont("LiberationSans", font_size)

    x = int(round((screen_w - font.size(TEXT)[0]) / 2.0))
    y = int(round(((screen_h - font.size(TEXT)[1]) / 2.0)))
    position = (x, y)

    return position, font

CTRL_U = u'\x15'

TEXT = ''
def keydown(event):
    ''' when a key is pressed '''
    global TEXT

    if event.key == pygame.K_BACKSPACE:
        if not TEXT:
            return
        TEXT = TEXT[:-1]
    # ctrl+U to clear screen
    elif event.unicode == CTRL_U:
        TEXT = ''
    else:
        TEXT = TEXT + event.unicode

    screen.fill(WHITE)

    if not TEXT:
        return

    position, font = get_font(TEXT)

    antialias = True

    tokens = nltk.word_tokenize(TEXT)
    # add back spaces that tokenize removed
    words = []
    total = ''
    for i, token in enumerate(tokens):
        if re.match(re.escape(total)+re.escape(token)+' ', TEXT):
            token = token + ' '
        words.append(token)
        total = total+token

    prev_word_end = position[0]
    for word in words:
        label = font.render(word, antialias, word_colour(word.strip()))
        word_position = (prev_word_end, position[1])
        screen.blit(label, word_position)
        prev_word_end += font.size(word)[0]


EVENTS = {
    pygame.QUIT: exit,
    pygame.KEYDOWN: keydown,
}


clock = pygame.time.Clock()
pygame.display.update()
while True:
    for event in pygame.event.get():
        EVENTS.get(event.type, noop)(event)
    pygame.display.update()