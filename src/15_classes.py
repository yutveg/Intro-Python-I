# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE


class LatLon:
    def __init__(self, lat=41.70505, lon=-121.51521):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name + ", " + str(self.lat) + ", " + str(self.lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, difficulty, size):
        self.difficulty = difficulty
        self.size = size
        super().__init__()


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
newWayPoint = Waypoint("Catacombs")
print(newWayPoint.__str__())
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
newGeoCache = Geocache()
# Print it--also make this print more nicely
# print(geocache)
