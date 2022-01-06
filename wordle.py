from wordle_strat_a import StratA
from wordle_strat_base import StratBase

from time import time

def get_fives():
    fives = []

    uplets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open('words.txt') as f:
        for line in f:
            word = line.rstrip()
            
            if len(word) != 5 or any(c not in uplets for c in word.upper()):
                continue

            fives.append(word.upper())

    return fives


def score_word(strategy, word, fiveset):
    strategy.reset()
    
    for guessnum in range(1, 7):
        guess = strategy.guess()
        
        if guess == word:
            return guessnum

        feedback = [-2] * 5 if guess not in fiveset else [1 if guess[i] == word[i] else 0 if guess[i] in word else -1 for i in range(5)]
        strategy.learn(feedback)

    return -1


def score_strategy(strategy, fives):
    fiveset = set(fives)
    good = 0
    bad = 0
    guesses = 0
    t = time()

    for i, word in enumerate(fives):
        if i > 0 and i % 1000 == 0:
            print(f'Played another 1000 words in {round(time()-t,2)} seconds. Have solved {good} out of {good+bad}')
            t = time()
        score = score_word(strategy, word, fiveset)

        if score == -1:
            bad += 1            
        else:
            good += 1
            guesses += score

    return (good, bad, guesses)

fives = get_fives()
strategies = [StratA(fives)]

for strategy in strategies:
    print(f'Scoring strategy: {strategy.name()}. Will play {len(fives)} words.')
    good, bad, guesses = score_strategy(strategy, fives)
    print(f'{strategy.name()} solved {good} out of {good+bad} ({round(100*good/(good+bad))}%) with an average number of {0 if good == 0 else round(guesses/good, 2)} guesses per success.')
    print()