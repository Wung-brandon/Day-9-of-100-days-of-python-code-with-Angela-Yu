
#nesting a list and dictionary inside a dictionary
travel = {
    "cameroon":{"towns_visited": ["buea","limbe","yaounde","mamfe","bamenda","douala","fontem"],"totally_visited":7},
    "not_visited": ["kumba","ngouandere","tiko"]
}

#nesting dictionary in a list
travel_log = [
    {"country": "cameroon",
     "towns_visited":["buea","bamenda","douala","fontem"],
     "total_visited":12},
    {"name":"brandon",
     "gender":"male",
     "age":20}
]

#function to add a new value of dictionaries to a list
def add_new_dict(country,visit,town):
    new_country = {}
    new_country["country"] = country
    new_country["towns_visit"] = visit
    new_country["towns_visited"] = town
    travel_log.append(new_country)
    print(travel_log)
    
add_new_dict(country="USA",visit=4,town=["ohio","las vargas","dallas"])    
       
