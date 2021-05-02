import datetime

COMM = 'Communication'
UTIL = 'Utilities'
ENER = 'Energy'
RE = 'Real_Estate'
CONS = 'Cons_Staples'
HC = 'Healthcare'
FIN = 'Financials'
IND = 'Industrials'
MAT = 'Materials'
COND = 'Cons_Disc'
IT = 'Info_Tech'

IDEAL_RATIOS = {
    COMM: 0.144623,
    UTIL: 0.146204,
    ENER: 0.067658,
    RE: 0.075623,
    CONS: 0.153964,
    HC: 0.127841,
    FIN: 0.036614,
    IND: 0.049434,
    MAT: 0.088559,
    COND: 0.062321,
    IT: 0.047160
}

SECTORS = [COMM, UTIL, ENER, RE, CONS, HC, FIN, IND, MAT, COND, IT]

class Portfolio():

    """
    Initialize Portfolio object with positions and their quantities. Initialize
    the amt_categories dictionary (used to keep track of how many positions of 
    each category are in the portfolio). 

    Parameters:
        w_to_change: int 
        timeline: int
        positions: (string, int) list 

    Returns: 
        Portfolio Object 
    """
    def __init__(self):
        self.amt_categories = {
            COMM: 100,
            UTIL: 100,
            RE: 100,
            CONS: 100,
            HC: 100,
            FIN: 100,
            IND: 100,
            MAT: 100,
            COND: 100,
            IT: 100
        }


    """
    Returns the current values of each sector.

    Parameter:
        date: datetime.datetime

    Returns:
        {string: float} dict
    """
    def get_sector_values(self, date):
        return {
            COMM: 0,
            UTIL: 0,
            RE: 0,
            CONS: 0,
            HC: 0,
            FIN: 0,
            IND: 0,
            MAT: 0,
            COND: 0,
            IT: 0
        }


    """
    Returns the current value of the portfolio.

    Parameter:
        date: datetime.datetime

    Returns:
        int
    """
    def get_portfolio_value(self, date):
        value = 0 
        for p in self.amt_categories:
            value += self.amt_categories[p]
        return value


    """
    Updates the amt_categories attribute of the current portfolio to reach the 
    'ideal' distribution again.

    Parameter:
        date: datetime.datetime
    """
    def rebalance_portfolio(self, date):
        portfolio_value = self.get_portfolio_value(date)
        amts_to_invest = {}
        for s in SECTORS:
            amt_sector = portfolio_value * IDEAL_RATIOS[s]
            amts_to_invest[s] = amt_sector
        self.amt_categories = amts_to_invest


