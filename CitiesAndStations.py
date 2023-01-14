def flatlandSpaceStations(n, c):
    if n == len(c):
        return 0
    
    c.sort()
    min_roads = []
        
    for i in range(0, n):
        if i not in c:
            min_road = findNearestStation(i, c, n)
            min_roads.append(min_road)
    
    return max(min_roads)
    
def findNearestStation(city, stations, number_of_cities):
    min_road = number_of_cities
    
    for i in range(0, len(stations)):
        road = abs(stations[i] - city)
        if road < min_road:
            min_road = road
    return min_road