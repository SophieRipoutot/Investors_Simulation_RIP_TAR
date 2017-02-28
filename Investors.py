import random   # to use the random function
import bonds
import Stocks


class Investor (object):

    def __init__(self, budget, mode, start):
        self.budget = budget                    # given budget
        self.mode = mode                        # mode of the investor
        self.start = start                      # start of the investment

    def mode(self):                             #we determine the mode of the investors
        list_mode = []
        if self.mode == 'aggressive':
            self.mode = list_mode[0]
        if self.mode == 'defensive':
            self.mode = list_mode[1]
        if self.mode == 'mixed':
            self.mode = list_mode[2]

    def defensive(self):
        if self.mode == 'defensive':
            while self.budget >= self.amount:
                investor_choice = random.randint(0, 1)
                self.budget = investorchoice * STBond.amount + (1 - investorchoice) * LTBond.amount

    def aggressive(self):
        if self.mode == 'aggressive':
            list_companies=["AAPL", "AXP", "FDX", "GOOGL", "IBM", "KO", "MS", "IOK", "XOM", "YHOO"]
            choice_stock = random.list_companies
            while self.budget > 100:
                qty = random.randint(0, (self.budget/stock.price)/2)
                self.budget = stock.price * qty

    def mixed(self):                                    # just idea
        if self.mode == "mixed":
            self.budget = 0.5 * defensive(self.budget) + 0.5 * aggressive(self.budget)
