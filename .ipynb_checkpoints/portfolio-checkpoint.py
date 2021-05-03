import sectordata
import hrp

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
        start_amount: int 

    Returns: 
        Portfolio Object 
    """
    def __init__(self, start_amount):
        self.last_update = '2011-04-01'
        self.amt_categories = {
            COMM: start_amount,
            UTIL: start_amount,
            ENER: start_amount,
            RE: start_amount,
            CONS: start_amount,
            HC: start_amount,
            FIN: start_amount,
            IND: start_amount,
            MAT: start_amount,
            COND: start_amount,
            IT: start_amount
        }


    """
    Returns the current values of each sector.

    Parameter:
        date: string (format: YYYY-MM-DD)

    Returns:
        {string: float} dict
    """
    def get_sector_values(self, date):
        sector_values = {}
        for s in SECTORS:
            val = sectordata.get_sector_value(s, date)
            sector_values[s] = val 
        return sector_values


    """
    Returns the current value of the portfolio.

    Parameter:
        date: string (format: YYYY-MM-DD)

    Returns:
        int
    """
    def get_portfolio_value(self, date):
        value = 0 
        for s in SECTORS:
            amt_s = self.amt_categories[s]
            init_price = sectordata.get_sector_value(s, self.last_update)
            num_shares = amt_s / init_price 
            price_today = sectordata.get_sector_value(s, date)
            value_today = num_shares * price_today
            value += value_today
        return value 


    """
    Updates the amt_categories attribute of the current portfolio to reach the 
    'ideal' distribution again.

    Parameter:
        date: string (format: YYYY-MM-DD)
    """
    def rebalance_portfolio(self, date):
        data = sectordata.get_sectors_delta('2011-04-01', date)
        if not data.empty:
            del data['S&P_500']
            ratios = hrp.main(data)
        
            portfolio_value = self.get_portfolio_value(date)
            amts_to_invest = {}
            for s in SECTORS:
                amt_sector = portfolio_value * ratios[s]
                amts_to_invest[s] = amt_sector
            self.amt_categories = amts_to_invest
            self.last_update = date 


# p = Portfolio(100)
# p.rebalance_portfolio('3/31/2011')

# start = 0 
# for i in p.amt_categories:
#     start += p.amt_categories[i]

# print(f'Start: {p.amt_categories}\n\n')
# print(f'START: {start}\n')

# p.rebalance_portfolio('4/30/2021')

# print(f'End: {p.amt_categories}\n\n')

# final = 0 
# for i in p.amt_categories:
#     final += p.amt_categories[i]

# print(f'FINAL: {final}')
