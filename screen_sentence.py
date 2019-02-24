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

BLACK = 0,0,0
WHITE = 255,255,255

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
    ratio = (test_font.size(text)[0] / float(len(text))) / 10.0
    font_size = int(round(min((screen_w/ratio) / len(text), screen_h )))
    font = pygame.font.SysFont("LiberationSans", font_size)

    x = int(round((screen_w - font.size(text)[0]) / 2.0))
    y = int(round(((screen_h - font.size(text)[1]) / 2.0)))
    position = (x, y)

    return position, font

def log_tags(tags):
    pretty_tags = ['{word}<{tag}>'.format(word=word, tag=tag) if len(tag) > 1 else word for word, tag in tags]
    logger.info( ' '.join(pretty_tags) )


class ScreenSentence(object):

    screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    screen.fill(WHITE)

    def clear_text(self, event):
        ''' clear all text from the screen '''
        self.text = ''

    def backspace(self, event):
        ''' remove last character '''
        if self.text:
            self.text = self.text[:-1]

    KEYBINDINGS = {
        pygame.K_BACKSPACE: backspace,
    }

    CTRL_KEYBINDINGS = {
        pygame.K_u: clear_text,
    }

    _text = ''
    antialias = True

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if value == self.text:
            return

        self._text = value
        self.redraw()

        # log if end of a word
        if re.match('[.!?]', event.unicode):
            tokens = nltk.word_tokenize(self.text)
            tags = nltk.pos_tag(tokens)
            log_tags(tags)

    def display_key(self, event):
        ''' key pressed wants to be shown on the screen '''

        self.text = self.text + event.unicode

    def keydown(self, event):
        ''' when a key is pressed '''

        if event.key in self.KEYBINDINGS:
            self.KEYBINDINGS[event.key](self, event)
        elif event.mod & pygame.KMOD_CTRL and event.key in self.CTRL_KEYBINDINGS:
            self.CTRL_KEYBINDINGS[event.key](self, event)
        else:
            self.display_key(event)

    def resize(event):
        logger.info('resize %s', event.size)
        self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        self.redraw()

    def redraw(self):

        self.screen.fill(WHITE)

        if not self.text:
            return

        position, font = get_font(self.text)

        tokens = nltk.word_tokenize(self.text)
        tags = nltk.pos_tag(tokens)

        # add back spaces that tokenize removed
        words = []
        total = ''
        for i, token in enumerate(tokens):
            if re.match(re.escape(total)+re.escape(token)+' ', self.text):
                token = token + ' '
            words.append(token)
            total = total+token

        prev_word_end = position[0]
        for word, tag in zip(words, tags):
            label = font.render(word, self.antialias, word_colour(tag))
            word_position = (prev_word_end, position[1])
            self.screen.blit(label, word_position)
            prev_word_end += font.size(word)[0]


screen_sentence = ScreenSentence()


EVENTS = {
    pygame.QUIT: exit,
    pygame.KEYDOWN: screen_sentence.keydown,
    pygame.VIDEORESIZE: screen_sentence.resize,
}


pygame.display.update()
while True:
    for event in pygame.event.get():
        EVENTS.get(event.type, noop)(event)
    pygame.display.update()
