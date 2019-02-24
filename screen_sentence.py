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

screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
BLACK = 0,0,0
WHITE = 255,255,255
screen.fill(WHITE)

TAGS = word_class.create_tags_from_csv('word_class.csv')

def word_colour(tag):
    ''' given a tag, find the colour for syntax hilighting '''

    try:
        return TAGS.get(tag[1], TAGS['DEFAULT']).colour
    except KeyError:
        return BLACK


def exit(event):
    sys.exit()


def noop(*args, **kwargs):
    pass

def get_font(text):
    ''' (str,) -> (position, font)
    
        get the font, find the fontsize that will fill the screen
        get the position that will centre this text on the screen
    '''
    screen_w, screen_h = pygame.display.get_surface().get_size()
    test_font = pygame.font.SysFont("LiberationSans", 10)
    ratio = (test_font.size(TEXT)[0] / float(len(TEXT))) / 10.0
    font_size = int(round(min((screen_w/ratio) / len(TEXT), screen_h )))
    font = pygame.font.SysFont("LiberationSans", font_size)

    x = int(round((screen_w - font.size(TEXT)[0]) / 2.0))
    y = int(round(((screen_h - font.size(TEXT)[1]) / 2.0)))
    position = (x, y)

    return position, font

def log_tags(tags):
    pretty_tags = ['{word}<{tag}>'.format(word=word, tag=tag) if len(tag) > 1 else word for word, tag in tags]
    logger.info( ' '.join(pretty_tags) )

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

    # log if end of a word
    if re.match('[.!?]', event.unicode):
        tokens = nltk.word_tokenize(TEXT)
        tags = nltk.pos_tag(tokens)
        log_tags(tags)

    redraw()


def resize(event):
    global screen
    logger.info('resize %s', event.size)
    screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
    redraw()


def redraw():
    global TEXT

    screen.fill(WHITE)

    if not TEXT:
        return

    position, font = get_font(TEXT)

    antialias = True

    tokens = nltk.word_tokenize(TEXT)
    tags = nltk.pos_tag(tokens)

    # add back spaces that tokenize removed
    words = []
    total = ''
    for i, token in enumerate(tokens):
        if re.match(re.escape(total)+re.escape(token)+' ', TEXT):
            token = token + ' '
        words.append(token)
        total = total+token

    prev_word_end = position[0]
    for word, tag in zip(words, tags):
        label = font.render(word, antialias, word_colour(tag))
        word_position = (prev_word_end, position[1])
        screen.blit(label, word_position)
        prev_word_end += font.size(word)[0]


EVENTS = {
    pygame.QUIT: exit,
    pygame.KEYDOWN: keydown,
    pygame.VIDEORESIZE: resize,
}


clock = pygame.time.Clock()
pygame.display.update()
while True:
    for event in pygame.event.get():
        EVENTS.get(event.type, noop)(event)
    pygame.display.update()
