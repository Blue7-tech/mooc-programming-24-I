# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    with open(filename) as file:
        list1 = []
        for line in file:
            parts = line.split(";") 
            if parts[0] == "Longitude":
                continue
            for i in range(0, len(parts)):
                if i == 0 or i == 1:
                    list1.append(float(parts[i]))
                    continue
                if i == 2 or i == 4:
                    list1.append(int(parts[i]))
                    continue
                if i == 6:
                    list1.append((parts[i].strip()))
                    break
                list1.append(parts[i])
    
    c = 3
    stations = {}
    for i in range(0,len(list1)):
        if i == 0:
            a = i
        elif i == 1:
            b = i
        elif i == c:
            stations[list1[i]] = (list1[a],list1[b])
            a += 7
            b += 7
            c += 7
    return stations

def distance(stations: dict, station1: str, station2: str):
    
    import math
        
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km
    
def greatest_distance(stations: dict):
    
    distances = []
    import math
    for key, value in stations.items():
        a = value[0]
        b = value[1]
        c = key
        for key, value in stations.items():
            if key != c:
                x_km = (a - value[0]) * 55.26
                y_km = (b - value[1]) * 111.2
                distance_km = math.sqrt(x_km**2 + y_km**2)
                t = (c, key, distance_km)
                distances.append(t) 
        else: 
            continue
    temp = ("","", 0)
    for tuple in distances:
        if tuple[2] > temp[2]:
            temp = tuple
    
    return temp        
   
    
if __name__ == "__main__":    
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
    


        
