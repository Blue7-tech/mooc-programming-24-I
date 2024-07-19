# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_object = {}
    
    movie_object["name"] = name
    movie_object["director"] = director
    movie_object["year"] = year
    movie_object["runtime"] = runtime
    
    database.append(movie_object)
    
if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)