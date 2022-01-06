class StratBase:
    def __init__(self, fives):
        self.fives = fives
        pass

    def reset(self):
        pass

    def name(self):
        return 'Strategy Base'

    def guess(self):
        return 'ABCDE'

    def learn(self, feedback):
        pass