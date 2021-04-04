import requests
import json 

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"


headers = {
    'x-rapidapi-key': "8c1dea45d1mshf68481c4f40bdc2p19580bjsnfeafc8fd25ba",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }






"""
Uses the values determined from the determine_new_quantities function in order 
to look through Yahoo finance API and find stocks within the desired category
that are labeled as 'Strong buys' to recommend to the user. 

Returns:
    {string: int} dict
"""
def determine_strong_buys(num_cat_buys):
    pass

"""
Ranks potential stocks to buy based on Yahoo Finance's current recommendation 
system. 

Parameters:
    potentials: string list 

Returns:
    {string: float} dict 
"""
def rank_potential_buys(potentials):
    weightings = {}
    for p in potentials:
        querystring = {"symbol":p,"region":"US"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        d = json.loads(response.text)
        for i in d['recommendationTrend']['trend']: 
            if i['period'] == '0m':
                print(f'{p}: {i}')
                w = 5*i['strongBuy'] + 3*i['buy'] - 3*i['sell'] - 5*i['strongSell']
                tot_a = i['strongBuy'] + i['buy'] + i['hold'] + i['sell'] + i['strongSell']
                weightings[p] = w/tot_a
    
    return weightings 




    
