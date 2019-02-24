from collections import namedtuple
import csv

BLACK = (0,0,0)

WordClass = namedtuple(
    'WordClass',
    'desc colour',
)
WordClass.__new__.__defaults__ = ('no description', BLACK)


def format_colour(s):
    ''' (str,) -> (int, int, int)

        take a colour format from the csv which is 3 numbers , separated and
        return a pygame colour.
    '''
    return tuple( int(i) for i in s.split(',') )


def create_tags_from_csv(f_name):
    ''' (str,) -> dict of WordClass

        read a csv and return WordClass tuples
    '''
    tags = {}
    with open(f_name) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            tags[row['TAG']] = WordClass(row['DESCRIPTION'], format_colour(row['COLOUR']))
    return tags
