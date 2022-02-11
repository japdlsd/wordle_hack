# Wordle Hack: solver of Wordle

This is a program which can play Worlde for you :)

## Install (you don't have to, but if you insist ...)

```shell
cd data
bash make_thesaurus.sh
```

## Usage

```shell
cd src/
python optimal_player.py
```

1. Run the program
2. Wait for the program to produce its guess
3. Type the guess into Wordle
4. If the word is not in the dictionary, just hit `Enter`
5. If the word is accepted, type the result ('g' for green, 'y' for yellow, 'w' for grey)
6. Goto step 2