class StratA:
    def __init__(self, fives):
        self.fives = self.order_fives(fives)
        self.reset()

    def name(self):
        return 'Strategy A'

    def order_fives(self, fives):
        # Based on https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
        letscores = {
            'E': 11.16,
            'A': 8.5,
            'R': 7.58,
            'I': 7.54,
            'O': 7.16,
            'T': 6.95,
            'N': 6.65,
            'S': 5.73,
            'L': 5.49,
            'C': 4.54,
            'U': 3.63,
            'D': 3.38,
            'P': 3.17,
            'M': 3.01,
            'H': 3.0,
            'G': 2.47,
            'B': 2.07,
            'F': 1.81,
            'Y': 1.78,
            'W': 1.29,
            'K': 1.10,
            'V': 1.01,
            'X': 0.29,
            'Z': 0.27,
            'J': 0.2,
            'Q': 0.2
        }

        scored = []

        for five in fives:
            score = sum(letscores[c] for c in set(five))
            scored.append((five, score))

        scored.sort(key=lambda w: -w[1])

        return [w[0] for w in scored]

    def reset(self):
        self.knowledge = {letter: set(range(5)) for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        self.definite = ['' for _ in range(5)]
        self.guesses = []

    def guess(self):        
        if all(c for c in self.definite):
            return ''.join(self.definite)

        if len(self.guesses) < 3:
            for five in self.fives:
                if any(len(self.knowledge[c]) < 5 for c in five):
                    continue

                guess = five
                break
        else:
            for five in self.fives:
                if any((i not in self.knowledge[five[i]]) or (self.definite[i] and self.definite[i] != five[i]) for i in range(5)):
                    continue

                guess = five
                break

        self.guesses.append(guess)
        return guess

    def learn(self, feedback):
        last_guess = self.guesses[-1]

        for i in range(5):
            if feedback[i] == 1:
                self.definite[i] = last_guess[i]
            elif feedback[i] == 0:
                self.knowledge[last_guess[i]].discard(i)
            elif feedback[i] == -1:
                self.knowledge[last_guess[i]] = set()