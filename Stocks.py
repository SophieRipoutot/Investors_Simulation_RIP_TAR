import pandas as pd

# we import the data from csv files

AAPL = pd.read_csv('F:\Data\AAPL.csv', delimiter=';')
print(AAPL)

AXP = pd.read_csv('F:\Data\AXP.csv', delimiter=';')
print(AXP)

FDX = pd.read_csv('F:\Data\FDX.csv', delimiter=';')
print(FDX)

GOOGL = pd.read_csv('F:\Data\GOOGL.csv', delimiter=';')
print(GOOGL)

IBM = pd.read_csv('F:\Data\IBM.csv', delimiter=';')
print(IBM)
KO = pd.read_csv('F:\Data\KO.csv', delimiter=';')
print(KO)

MS = pd.read_csv('F:\Data\MS.csv', delimiter=';')
print(MS)

IOK = pd.read_csv('F:\Data\IOK.csv', delimiter=';')
print(IOK)

XOM = pd.read_csv('F:\Data\XOM.csv', delimiter=';')
print(XOM)

YHOO = pd.read_csv('F:\Data\YHOO.csv', delimiter=';')
print(YHOO)

# we create the class Stock

class Stock (object):
    def __init__(self, name, term, amount, number, date):
        self.name = name                            # name of the stock
        self.term = term                            # term during which the investment will be done
        self.amount = amount                        # certain invested amount
        self.number = number                        # number of stocks bought
        self.date = date                            # date at which the stock has been bought

# our purpose now is to assign the column High of csv files as price of stock
row_count = sum(1 for row in AAPL)
print(row_count)

row_count = 2547


#def price():
#    list_stock_price = []
 #   for i in range(1, row_count):
 #       list_stock_price.append(AAPLhigh(i))


class Buy(Stock):
    def __init__(self, name, term, amount, number, date, bs):
        list_bs = ['buy', 'sell']
        super(STBond, self).__init__(name, term, amount, number, date)
        self.bs = list_bs[0]
        self.name = name
        self.term = term
        self.amount = amount
        self.number = number
        self.date = date


class Sell (Stock):
    def __init__(self, name, term, amount, number, date, bs):
        list_bs = ['buy', 'sell']
        super(STBond, self).__init__(name, term, amount, number, date)
        self.bs = list_bs = [1]
        self.name = name
        self.term = term
        self.amount = amount
        self.number = number
        self.date = date