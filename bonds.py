class bond (object):

    def __init__(self, term, amount, min_price, min_term, rate, acc_amount, nb_compounded, category):
        self.term = term                # a term we'll invest in
        self.amount = amount            # a certain amount invested in
        self.min_price = min_price      # a minimum price of the bond
        self.min_term = min_term        # a minimum term
        self.rate = rate                # a yearly interest rate
        self.acc_amount = acc_amount    # accumulated amount
        self.nb_compounded = nb_compounded        # number of times the interest is compounded by year
        self.category = category        # type of bond (short term, long term)

# short term bonds have a minimum of 2 years, min amount of 1000 and yearly interest rate of 1%


class Typebond (bond):
    def __init__(self):
        super().__init__()  # get attributes of the mother class
        self.type = []
        self.category = ['Short term', 'Long term']

# we define the short term and long term type for bonds
# we create methods from the attributes of the class bond

    def st_bond(self):
        if self.term < 2:
            if self.amount >= 2:
                if self.amount <= 5:
                    if self.rate == 0.01:
                        self.type = [1]
                        return self.type

    def lt_bond(self):
        if self.term >= 5:
            if self.amount >= 3000:
                if self.rate == 0.03:
                    self.type = [2]
                    return self.type

# both are compounded yearly and have a way to calculate the compounded interest rate for a certain time t
# create a function that allows to calculate the compounded interest rate at anytime time t

    def comp_rate(self):
        self.nb_compounded = 1
        self.acc_amount = 0.00
        self.acc_amount = self.amount * (1 + self.rate/self.nb_compounded)











