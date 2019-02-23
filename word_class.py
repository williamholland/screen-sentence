from collections import namedtuple

# colour scheme
# https://www.color-hex.com/color-palette/73968
CS = {
    'verb': (65,199,162),
    'adj': (249,77,68),
    'default': (223,236,15),
    #(236,232,232), #too bright
    'noun': (2,2,2),
}


WordClass = namedtuple(
    'WordClass',
    'desc colour',
)
WordClass.__new__.__defaults__ = ('no description', CS['default'])

DEFAULT = WordClass()

TAGS = {
    "CC":   WordClass("coordinating conjunction",),
    "CD":   WordClass("cardinal digit",),
    "DT":   WordClass("determiner",),
    "EX":   WordClass("existential there",),
    "FW":   WordClass("foreign word",),
    "IN":   WordClass("preposition/subordinating conjunction",),
    "JJ":   WordClass("adjective (large)", CS['adj']),
    "JJR":  WordClass("adjective, comparative (larger)", CS['adj']),
    "JJS":  WordClass("adjective, superlative (largest)", CS['adj']),
    "LS":   WordClass("list market",),
    "MD":   WordClass("modal (could, will)",),
    "NN":   WordClass("noun, singular (cat, tree)", CS['noun']),
    "NNS":  WordClass("noun plural (desks)", CS['noun']),
    "NNP":  WordClass("proper noun, singular (sarah)", CS['noun']),
    "NNPS": WordClass("proper noun, plural (indians or americans)", CS['noun']),
    "PDT":  WordClass("predeterminer (all, both, half)",),
    "POS":  WordClass("possessive ending (parent's)",),
    "PRP":  WordClass("personal pronoun (hers, herself, him,himself)", CS['noun']),
    "PRP$": WordClass("possessive pronoun (her, his, mine, my, our )", CS['noun']),
    "RB":   WordClass("adverb (occasionally, swiftly)",),
    "RBR":  WordClass("adverb, comparative (greater)",),
    "RBS":  WordClass("adverb, superlative (biggest)",),
    "RP":   WordClass("particle (about)",),
    "TO":   WordClass("infinite marker (to)",),
    "UH":   WordClass("interjection (goodbye)",),
    "VB":   WordClass("verb (ask)", CS['verb']),
    "VBG":  WordClass("verb gerund (judging)", CS['verb']),
    "VBD":  WordClass("verb past tense (pleaded)", CS['verb']),
    "VBN":  WordClass("verb past participle (reunified)", CS['verb']),
    "VBP":  WordClass("verb, present tense not 3rd person singular(wrap)", CS['verb']),
    "VBZ":  WordClass("verb, present tense with 3rd person singular (bases)", CS['verb']),
    "WDT":  WordClass("wh-determiner (that, what)",),
    "WP":   WordClass("wh- pronoun (who)",),
    "WRB":  WordClass("wh- adverb (how) ",),
}
