# Screen Sentence

Inspired by [screen message](https://screenmessage.com/) but with English
language syntax highlighting.

Designed as an EFL teaching aid that allows for impromptu live demonstrations.

## Demo

![demo.gif](https://github.com/williamholland/screen-sentence/blob/master/img/demo.gif)

## Requirements

To run this script you will need:

    * pygame
    * nltk

## Colour Meanings

The colours of each word comes from a tag assigned by `nltk`. The colour of
each tag can be configured in `word_class.csv`. The colour comes from the comma
separated list of red,green,blue values in the COLOUR column. The default
colours as shown in the table below.


| TAG | DESCRIPTION | COLOUR |
| --- | ----------- | ------ |
| `DEFAULT` | default colour | ![#555753](https://placehold.it/15/555753/000000?text=+) `85,87,83` |
| `CC` | coordinating conjunction | ![#555753](https://placehold.it/15/555753/000000?text=+) `85,87,83` |
| `CD` | cardinal digit | ![#555753](https://placehold.it/15/555753/000000?text=+) `85,87,83` |
| `DT` | determiner | ![#33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `51,195,193` |
| `EX` | existential there | ![#33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `51,195,193` |
| `FW` | foreign word | ![#555756](https://placehold.it/15/555756/000000?text=+) `85,87,86` |
| `IN` | preposition/subordinating conjunction | ![#fa701d](https://placehold.it/15/fa701d/000000?text=+) `250,112,29` |
| `JJ` | adjective (large) | ![#9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `159,0,189` |
| `JJR` | adjective, comparative (larger) | ![#9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `159,0,189` |
| `JJS` | adjective, superlative (largest) | ![#9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `159,0,189` |
| `LS` | list market | ![#55575b](https://placehold.it/15/55575b/000000?text=+) `85,87,91` |
| `MD` | modal (could, will) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `NN` | noun, singular (cat, tree) | ![#135cd0](https://placehold.it/15/135cd0/000000?text=+) `19,92,208` |
| `NNS` | noun plural (desks) | ![#135cd0](https://placehold.it/15/135cd0/000000?text=+) `19,92,208` |
| `NNP` | proper noun, singular (sarah) | ![#135cd0](https://placehold.it/15/135cd0/000000?text=+) `19,92,208` |
| `NNPS` | proper noun, plural (indians or americans) | ![#135cd0](https://placehold.it/15/135cd0/000000?text=+) `19,92,208` |
| `PDT` | predeterminer (all, both, half) | ![#f8282a](https://placehold.it/15/f8282a/000000?text=+) `248,40,42` |
| `POS` | possessive ending (parent's) | ![#1670ff](https://placehold.it/15/1670ff/000000?text=+) `22,112,255` |
| `PRP` | personal pronoun (hers, herself, him,himself) | ![#1670ff](https://placehold.it/15/1670ff/000000?text=+) `22,112,255` |
| `PRP$` | possessive pronoun (her, his, mine, my, our ) | ![#1670ff](https://placehold.it/15/1670ff/000000?text=+) `22,112,255` |
| `RB` | adverb (occasionally, swiftly) | ![#328a5d](https://placehold.it/15/328a5d/000000?text=+) `50,138,93` |
| `RBR` | adverb, comparative (greater) | ![#328a5d](https://placehold.it/15/328a5d/000000?text=+) `50,138,93` |
| `RBS` | adverb, superlative (biggest) | ![#328a5d](https://placehold.it/15/328a5d/000000?text=+) `50,138,93` |
| `RP` | particle (about) | ![#555768](https://placehold.it/15/555768/000000?text=+) `85,87,104` |
| `TO` | infinite marker (to) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `UH` | interjection (goodbye) | ![#55576a](https://placehold.it/15/55576a/000000?text=+) `85,87,106` |
| `VB` | verb (ask) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `VBG` | verb gerund (judging) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `VBD` | verb past tense (pleaded) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `VBN` | verb past participle (reunified) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `VBP` | verb, present tense not 3rd person singular(wrap) | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `44,198,49` |
| `VBZ` | verb, present tense with 3rd person singular (bases) | ![#555770](https://placehold.it/15/555770/000000?text=+) `85,87,112` |
| `WDT` | wh-determiner (that, what) | ![#555771](https://placehold.it/15/555771/000000?text=+) `85,87,113` |
| `WP` | wh- pronoun (who) | ![#555772](https://placehold.it/15/555772/000000?text=+) `85,87,114` |
| `WRB` | wh- adverb (how)  | ![#328a5d](https://placehold.it/15/328a5d/000000?text=+) `50,138,93` |

## TODO

* manual adjustments
