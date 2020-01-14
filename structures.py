directions = [
    ("ALA", "TSE"),
    ("TSE", "ALA"),
    ("ALA", "MOW"),
    ("MOW", "ALA"),
    ("ALA", "CIT"),
    ("CIT", "ALA"),
    ("TSE", "MOW"),
    ("MOW", "TSE"),
    ("TSE", "LED"),
    ("LED", "TSE"),  
]
tickets = {
    directions[0] : None,
    directions[1] : None,
    directions[2] : None,
    directions[3] : None,
    directions[4] : None,
    directions[5] : None,
    directions[6] : None,
    directions[7] : None,
    directions[8] : None,
    directions[9] : None,
}

cache = { "data" : {
    ("ALA", "TSE"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("TSE", "ALA"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],
    
    ("ALA", "MOW"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("MOW", "ALA"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("ALA", "CIT"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("CIT", "ALA"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("TSE", "MOW"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("MOW", "TSE"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],

    ("TSE", "LED"): [{"adults": 1, "infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": [],}],
    ("LED", "TSE"): [{"adults": 1,"infants": 1, "children": 1, "tickets": [], "low_price": []}, 
                     {"adults": 1, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 1, "infants": 0, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 1, "children": 0, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 1, "tickets": [], "low_price": []},
                     {"adults": 2, "infants": 0, "children": 0, "tickets": [], "low_price": []},],}
    }
