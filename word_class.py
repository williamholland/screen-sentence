from collections import namedtuple
import csv

BLACK = (0,0,0)

WordClass = namedtuple(
    'WordClass',
    'desc colour',
)
WordClass.__new__.__defaults__ = ('no description', BLACK)

DEFAULT = WordClass('not a word', BLACK)

TAGS = {}

def format_colour(s):
    ''' (str,) -> (int, int, int) '''
    return tuple( int(i) for i in s.split(',') )

with open('word_class.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        print row
        TAGS[row['TAG']] = WordClass(row['DESCRIPTION'], format_colour(row['COLOUR']))
