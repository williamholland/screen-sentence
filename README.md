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

## TODO

* manual adjustments


| TAG | DESCRIPTION | COLOUR |
| --- | ----------- | ------ |
| `DEFAULT` | default colour | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `CC` | coordinating conjunction | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `CD` | cardinal digit | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `DT` | determiner | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `EX` | existential there | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `FW` | foreign word | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `IN` | preposition/subordinating conjunction | - ![#ffd74c](https://placehold.it/15/ffd74c/000000?text=+) `255,215,76` |
| `JJ` | adjective (large) | - ![#729fcf](https://placehold.it/15/729fcf/000000?text=+) `114,159,207` |
| `JJR` | adjective, comparative (larger) | - ![#204a87](https://placehold.it/15/204a87/000000?text=+) `32,74,135` |
| `JJS` | adjective, superlative (largest) | - ![#729fcf](https://placehold.it/15/729fcf/000000?text=+) `114,159,207` |
| `LS` | list market | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `MD` | modal (could, will) | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
| `NN` | noun, singular (cat, tree) | - ![#ff4040](https://placehold.it/15/ff4040/000000?text=+) `255,64,64` |
| `NNS` | noun plural (desks) | - ![#ff4040](https://placehold.it/15/ff4040/000000?text=+) `255,64,64` |
| `NNP` | proper noun, singular (sarah) | - ![#ff4040](https://placehold.it/15/ff4040/000000?text=+) `255,64,64` |
| `NNPS` | proper noun, plural (indians or americans) | - ![#ff4040](https://placehold.it/15/ff4040/000000?text=+) `255,64,64` |
| `PDT` | predeterminer (all, both, half) | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `POS` | possessive ending (parent's) | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `PRP` | personal pronoun (hers, herself, him,himself) | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `PRP$` | possessive pronoun (her, his, mine, my, our ) | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `RB` | adverb (occasionally, swiftly) | - ![#ad7fa8](https://placehold.it/15/ad7fa8/000000?text=+) `173,127,168` |
| `RBR` | adverb, comparative (greater) | - ![#5c3566](https://placehold.it/15/5c3566/000000?text=+) `92,53,102` |
| `RBS` | adverb, superlative (biggest) | - ![#ad7fa8](https://placehold.it/15/ad7fa8/000000?text=+) `173,127,168` |
| `RP` | particle (about) | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `TO` | infinite marker (to) | - ![#ff66cc](https://placehold.it/15/ff66cc/000000?text=+) `255,102,204` |
| `UH` | interjection (goodbye) | - ![#cdc8b1](https://placehold.it/15/cdc8b1/000000?text=+) `205,200,177` |
| `VB` | verb (ask) | - ![#76ee00](https://placehold.it/15/76ee00/000000?text=+) `118,238,0` |
| `VBG` | verb gerund (judging) | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
| `VBD` | verb past tense (pleaded) | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
| `VBN` | verb past participle (reunified) | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
| `VBP` | verb, present tense not 3rd person singular(wrap) | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
| `VBZ` | verb, present tense with 3rd person singular (bases) | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
| `WDT` | wh-determiner (that, what) | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `WP` | wh- pronoun (who) | - ![#ff6a6a](https://placehold.it/15/ff6a6a/000000?text=+) `255,106,106` |
| `WRB` | wh- adverb (how)  | - ![#9bcd9b](https://placehold.it/15/9bcd9b/000000?text=+) `155,205,155` |
