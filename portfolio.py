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
    def __init__(self, w_to_change, timeline, positions):
        self.willing_to_change = w_to_change
        self.timeline = timeline
        self.quant_positions = {}
        self.num_positions = len(positions)
        self.amt_categories = {
            'c1': 0,
            'c2': 0,
            'c3': 0,
            'c4': 0,
            'c5': 0
        }
        self.new_category_ratios = {
            'c1': .2,
            'c2': .2,
            'c3': .2,
            'c4': .2,
            'c5': .2
        }


    """
    Uses static data to categorize the positions inside a portfolio. It updates
    the amt_categories dictionary within the Portfolio object. 
    """
    def categorize_positions(self):
        pass 

    """
    Uses the amt_categories attribute and num_positions attribute to determine 
    what the initial ratios for each category in the inital portfolio were. 

    Returns:
        {string: float} dict
    """
    def initial_cat_ratios(self):
        pass