This is a very early stages repository.

It deals with the very excellent game Wordle, found at https://www.powerlanguage.co.uk/wordle/

The author of this repository is in no way affiliated with the author(s) of Wordle.

Currently, there are five files of interest:

**wordle.py**

This is the main program. It currently accepts no command-line parameters or the like. Running the program will create a list of valid words and then score every strategy against every word. Mostly by keeping count of solved/unsolved words, but also by keeping track of the average number of guesses.

As things stand now, strategies will have to be added manually in code in order for them to be run. In a future version, this will likely happen through an argument passed to the script. Currently, only Strategy A will be run.

**wordle_strat_base.py**

A very rough interface that strategies must adhere to. A strategy needs to implement:

* a constructor
* a `reset()` method to be called before the run of every word
* a `name()` method that returns a string that identifies the strategy in printouts
* a `guess()` method that guesses a word when queried by the runner
* a `learn()` method that receives feedback from the runner after every guess

**wordle_strat_a.py**

A strategy that is being worked on, but currently solves 94% of the available words.

**words.txt**

A general purpose English dictionary from which the collection of five-letter words can be assembled.

**five_words.py**

The source of a smaller list of five-letter words. This is now the default choice.
