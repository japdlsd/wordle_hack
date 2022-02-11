#!/bin/bash

wget -O all_words.txt 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'

# filter only five letters long words
awk 'length == 6' all_words.txt > words5.txt