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

    def defensive(self):                        # we describe the behaviour of the defensive mode
        if self.mode == 'defensive':
            while self.budget >= self.amount:   # while the budget is greater than the minimum price of a short term bond
                investor_choice = random.randint(0, 1)  # the choice is determined by a random number between 0 and 1
                self.budget = investorchoice * STBond.amount + (1 - investorchoice) * LTBond.amount # he invests a part in short term bond and the other in long term bond

    def aggressive(self):                       # we describe the behaviour of the aggressive mode
        if self.mode == 'aggressive':
            list_companies=["AAPL", "AXP", "FDX", "GOOGL", "IBM", "KO", "MS", "IOK", "XOM", "YHOO"]
            choice_stock = random.list_companies  # he chooses randomly a stock among available companies stock
            while self.budget > 100:  # while the budget is greater than 100 dollars
                qty = random.randint(0, (self.budget/stock.price)/2) # the invested quantity is a number between 0 and the half max number of share he can buy
                self.budget = stock.price * qty

    def mixed(self):                                    # just idea : combination of defensive and aggressive mode
        if self.mode == "mixed":
            self.budget = 0.5 * defensive(self.budget) + 0.5 * aggressive(self.budget)
