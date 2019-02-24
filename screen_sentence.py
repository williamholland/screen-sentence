import re
import sys
import pygame
import nltk
import logging
import inspect
import types

import word_class

logging.basicConfig(format='%(asctime)s File %(name)s, line %(lineno)d, %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

pygame.init()

BLACK = 0,0,0
WHITE = 255,255,255
INFO_OBJECT = pygame.display.Info()
MONITOR_SIZE = (INFO_OBJECT.current_w, INFO_OBJECT.current_h)

TAGS = word_class.create_tags_from_csv('word_class.csv')

def word_colour(tag):
    ''' given a tag, find the colour for syntax hilighting '''

    try:
        return TAGS.get(tag[1], TAGS['DEFAULT']).colour
    except KeyError:
        return BLACK


def exit(event):
    ''' handle when the program exits '''
    logger.info('exit gracefully. Goodbye.')
    sys.exit()


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
    ''' take tags and log them in a compact way '''
    pretty_tags = ['{word}<{tag}>'.format(word=word, tag=tag) if len(tag) > 1 else word for word, tag in tags]
    logger.info( ' '.join(pretty_tags) )


class ScreenSentence(object):

    _fullscreen = False
    _text = ''
    _size = (600, 400)
    screen = pygame.display.set_mode(_size, pygame.RESIZABLE)
    screen.fill(WHITE)
    antialias = True

    def clear_text(self, event):
        ''' clear all text from the screen '''
        self.text = ''

    def clear_word(self, event):
        ''' clear last word '''
        if ' ' not in self.text:
            self.text = ''
        else:
            self.text = self.text.rsplit(' ', 1)[0]

    def backspace(self, event):
        ''' remove last character '''
        if self.text:
            self.text = self.text[:-1]

    def toggle_fullscreen(self, event):
        self.fullscreen = not self.fullscreen

    # functions to call when keys are pressed
    KEYBINDINGS = {
        pygame.K_BACKSPACE: backspace,
        pygame.K_ESCAPE: exit,
        pygame.K_F11: toggle_fullscreen,
    }

    # functions to call when keys are pressed with ctrl
    CTRL_KEYBINDINGS = {
        pygame.K_u: clear_text,
        pygame.K_w: clear_word,
        pygame.K_c: exit,
        pygame.K_d: exit,
    }

    def bind_keybindings(self):
        ''' bind the functions specified in keybindings to this instance, deep
            magic
        '''
        my_methods = [t[1] for t in inspect.getmembers(self, predicate=inspect.ismethod)]
        for key, f in self.KEYBINDINGS.items():
            bound_f = types.MethodType(f, self)
            if bound_f in my_methods and bound_f not in self.KEYBINDINGS:
                self.KEYBINDINGS[key] = bound_f
        for key, f in self.CTRL_KEYBINDINGS.items():
            bound_f = types.MethodType(f, self)
            if bound_f in my_methods and bound_f not in self.CTRL_KEYBINDINGS:
                self.CTRL_KEYBINDINGS[key] = bound_f

    def __init__(self):
        self.bind_keybindings()

    @property
    def fullscreen(self):
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        if value == self._fullscreen:
            return

        self._fullscreen = value
        if self._fullscreen:
            logger.info('fullscreen activated')
            self.screen = pygame.display.set_mode(MONITOR_SIZE, pygame.FULLSCREEN)
        else:
            logger.info('fullscreen deactivated')
            self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)

        self.redraw()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value == self._size:
            return
        self._size = value
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.redraw()

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
            self.KEYBINDINGS[event.key](event)
        elif event.mod & pygame.KMOD_CTRL and event.key in self.CTRL_KEYBINDINGS:
            self.CTRL_KEYBINDINGS[event.key](event)
        else:
            self.display_key(event)

    def resize(event):
        ''' the window has been resized, redraw the display

            note that this signal isn't always emmitted so appears buggy, this
            is a fault of pygame version in debian
        '''
        logger.info('resize %s', event.size)
        self.size = event.size

    def redraw(self):
        ''' update the display with the text '''

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


# This is how the program handles
EVENTS = {
    pygame.QUIT: exit,
    pygame.KEYDOWN: screen_sentence.keydown,
    pygame.VIDEORESIZE: screen_sentence.resize,
}


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type in EVENTS:
            EVENTS[event.type](event)
    pygame.display.update()
