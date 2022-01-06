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

## Sample run

```Scoring strategy: Strategy A. Will play 12972 words.
Played another 1000 words in 4.73 seconds. Have solved 957 out of 1000
Played another 1000 words in 4.65 seconds. Have solved 1928 out of 2000
Played another 1000 words in 4.67 seconds. Have solved 2892 out of 3000
Played another 1000 words in 5.28 seconds. Have solved 3827 out of 4000
Played another 1000 words in 5.07 seconds. Have solved 4777 out of 5000
Played another 1000 words in 5.45 seconds. Have solved 5685 out of 6000
Played another 1000 words in 5.36 seconds. Have solved 6568 out of 7000
Played another 1000 words in 5.04 seconds. Have solved 7472 out of 8000
Played another 1000 words in 4.84 seconds. Have solved 8432 out of 9000
Played another 1000 words in 4.67 seconds. Have solved 9360 out of 10000
Played another 1000 words in 5.02 seconds. Have solved 10224 out of 11000
Played another 1000 words in 5.42 seconds. Have solved 11151 out of 12000
Strategy A solved 11923 out of 12972 (92%) with an average number of 4.67 guesses per success.