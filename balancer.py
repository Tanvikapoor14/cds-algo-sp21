from portfolio import Portfolio

"""
Allows the user to input the positions that are currently in their portfolio. 

Returns:
    Portfolio object
"""
def input_portfolio():
    willing_to_change = float(input("Enter the percent of your portfolio you are willing to change: ").strip())
    timeline = float(input("Enter the number of years you plan on leaving your money in the stock market: ").strip())
    positions = {}
    while True:
        ticker = input("Enter the ticker for a stock: ").strip()
        quant = int(input("Enter the quantity of this stock in your portfolio: ").strip())
        done = input('Enter "d" if you are done. Press enter to continue: ').strip()

        positions[ticker] = quant
        if done == "d":
            break

    return Portfolio(willing_to_change, timeline, positions)


"""
Determines what the new proportions of each category of stock should be by 
running statistical tests using the attributes of the user's portfolio. This 
function updates the 'new_category_ratios' attribute of the Portfolio object. 

Parameters:
    portfolio: Portfolio object 
"""
def determine_new_balance(portfolio):
    pass


"""
Uses the initial_cat_ratios method and the new_category_ratios of a portfolio 
in order to determine how many stocks should be bought in each category. 

Returns:
    {string: int} dict
"""
def determine_new_quantities(portfolio):
    pass



def main():
    portfolio = input_portfolio()
    portfolio.categorize_positions()
    determine_new_balance(portfolio)
    new_quants = determine_new_quantites(portfolio)
    recomendations = determine_strong_buys(new_quants)

    for i in reccomendations:
        print(i)