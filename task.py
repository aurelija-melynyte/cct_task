"""
Flatland is a country with a number of cities, some of which have train stations. Cities are 
numbered consecutively and each has a road of 1km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. Determine 
the maximum distance from any city to its nearest train station.

Notes:
- Cities are indexed from 0.
- Number of cities is between 1 and 10000.
- Number of cities with train station is between 1 and number of cities.
- No city has more than one train station.

Example:

number_of_cities == 3
cities_with_train_station == [1]

There are 3 cities and city #1 has a train station. They occur consecutively along a route. 
City #0 is 1km away, city #1 is 0km away and city #2 is 1km away from its nearest train station.
The maximum distance is 1.

"""

from typing import List
import math


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:

    distances = []
    start_index = 0
    for city_index in cities_with_train_station:
        distance = city_index - start_index
        distances.append(distance)
        start_index = city_index + 1

    max_distance = math.ceil(max(distances) / 2)

    # checking the distances from first and last city to the nearest train station
    distance_from_first_city = distances[0]
    distance_from_last_city = number_of_cities - 1 - cities_with_train_station[-1]

    max_distance = max(distance_from_first_city, distance_from_last_city, max_distance)
    return max_distance


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    print("ALL TESTS PASSED")
