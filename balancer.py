"""
Allows the user to input the positions that are currently in their portfolio. 

Returns:
    Portfolio object
"""
def input_portfolio():
    #get % willing to change
    #get timeline 
    #while loop until done, takes in two data points (ticker, quantity)
    pass


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

"""
Uses the values determined from the determine_new_quantities function in order 
to look through Yahoo finance API and find stocks within the desired category
that are labeled as 'Strong buys' to recommend to the user. 

Returns:
    {string: int} dict
"""
def determine_strong_buys(num_cat_buys):
    pass


def main():
    portfolio = input_portfolio()
    portfolio.categorize_positions()
    determine_new_balance(portfolio)
    new_quants = determine_new_quantites(portfolio)
    recomendations = determine_strong_buys(new_quants)

    for i in reccomendations:
        print(i)