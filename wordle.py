from time import time
import five_words
from wordle_strat_a import StratA


def get_fives_big():
    fives = []

    uplets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open('words.txt') as file:
        for line in file:
            word = line.rstrip()

            if len(word) != 5 or any(c not in uplets for c in word.upper()):
                continue

            fives.append(word.upper())

    return fives


def get_fives_small():
    return list(map(lambda word: word.upper(), five_words.fives()))


def score_word(strategy, word, fiveset):
    strategy.reset()

    for guessnum in range(1, 7):
        guess = strategy.guess()

        if guess == word:
            return guessnum

        if guess not in fiveset:
            strategy.learn([-2] * 5)
            continue

        feedback = [1 if guess[i] == word[i] else 0 if guess[i] in word else -1 for i in range(5)]
        strategy.learn(feedback)

    return -1


def score_strategy(strategy, fives):
    fiveset = set(fives)
    good = 0
    bad = 0
    guesses = 0
    time_stamp = time()

    for i, word in enumerate(fives):
        if i > 0 and i % 1000 == 0:
            rounded_time = round(time()-time_stamp,2)
            message = f'Played another 1000 words in {rounded_time} seconds. Have solved {good} out of {good+bad}'
            print(message)
            time_stamp = time()
        score = score_word(strategy, word, fiveset)

        if score == -1:
            bad += 1
        else:
            good += 1
            guesses += score

    return (good, bad, guesses)

fives = get_fives_small()
strategies = [StratA(fives)]

for strategy in strategies:
    print(f'Scoring strategy: {strategy.name()}. Will play {len(fives)} words.')
    good, bad, guesses = score_strategy(strategy, fives)
    print(f'{strategy.name()} solved {good} out of {good+bad} ({round(100*good/(good+bad))}%) with an average number of {0 if good == 0 else round(guesses/good, 2)} guesses per success.')
    print()
