

def formatter(start, end, pattern="%d/%m/%Y"):
    try: 
        return [start.strftime(pattern), end.strftime(pattern)]
    except AttributeError:
        print("Use date only to get formatted data")



def get_min_price(index, firstTicket, fromTo, toFrom, d, secondTicket=None, a=None):   
    response = None
    cacheDeparture = []
    cacheArrival = []
    dLowest = None
    aLowest = None
    if a and secondTicket:
        for ti in firstTicket:    
            if ti[1] == d:
                cacheDeparture.append(ti)
        if len(cacheDeparture) == 0:
            response = f"No tickets for departure on {d}, try another day, or use correct date"
            return response
        
        for tic in secondTicket:
            if tic[1] == a:
                cacheArrival.append(tic)
        if len(cacheArrival) == 0:
            response = f"No tickets for arrival on {a}, try another day, or use correct date"
            return response        
    
        dLowest = cacheDeparture[0]
        dLowest = dLowest[0]
        aLowest = cacheArrival[0]
        aLowest = aLowest[0]
    else:
    
        for ti in firstTicket:            
            if ti[1] == d:
                cacheDeparture.append(ti)
              
        if len(cacheDeparture) == 0:
            response = f"No tickets for departure on {d}, try another day, or use correct date"
            return response      
        dLowest = cacheDeparture[0]
        dLowest = dLowest[0]
    if secondTicket:
        response = []
        ticket_Departure = None
        ticket_Arrival = None
        
        for t0 in cacheDeparture:
            dLowest = dLowest if dLowest <= t0[0] else t0[0]
        for t0 in cacheDeparture:
            if t0[0] == dLowest:
                ticket_Departure = t0      
        for t1 in cacheArrival:
            aLowest = aLowest if aLowest <= t1[0] else t1[0]
        for t1 in cacheArrival:
            if t1[0] == aLowest:
                ticket_Arrival = t1
        response.append(ticket_Departure)
        response.append(ticket_Arrival)
        response.append((fromTo, toFrom, index))
        return response    
    else:
        response = []
        ticket_Departure = None
        for t3 in cacheDeparture:
            dLowest = dLowest if dLowest <= t3[0] else t3[0]
        for t3 in cacheDeparture:
            if t3[0] == dLowest:
                ticket_Departure = t3
            response.append(ticket_Departure)
            response.append((fromTo, index))
            return response