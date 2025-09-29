# Wordle Hack: solver of Wordle

This is a program which can play Wordle for you :)

## Install

```bash
mamba env create -f environment.yaml #@TODO add environment file
mamba activate wordle

pip install -e .
```

## Usage

```shell
wordle
```

1. Run the program
2. Wait for the program to produce its guess
3. Type the guess into Wordle
4. If the word is not in the dictionary, just hit `Enter`
5. If the word is accepted, type the result ('g' for green, 'y' for yellow, 'w' for grey)
6. Goto step 2
