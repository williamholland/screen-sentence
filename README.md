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

![word\_class.png](https://github.com/williamholland/screen-sentence/blob/master/img/word_class.png)

## TODO

* multi-line
