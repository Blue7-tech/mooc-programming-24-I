import math 

def get_station_data(filename: str):
    stations = []
    with open(filename) as file:
        
        for line in file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            parts[0] = float(parts[0])
            parts[1] = float(parts[1])  
            stations.append(parts)
    
    dict_stations = {}
    for station in stations:
        dict_stations[station[3]] = (station[0], station[1])
            
    return dict_stations

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km

def greatest_distance(stations: dict):
    d_fin = 0
    station_a = ()
    station_b = ()
    for station1 in stations:
        for station2 in stations:
            d_km = distance(stations,station1,station2)
            if d_km > d_fin:
                d_fin = d_km
                station_a = station1
                station_b = station2

    return station_a, station_b, d_fin
            
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)