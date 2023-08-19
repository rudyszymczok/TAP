import itertools
from collections import Counter

class Knuth:

    def __init__(self, size_of_fleet, routes, no_of_flights):
        self.route_combinations = []
        self.size_of_fleet = size_of_fleet
        self.routes = routes
        self.no_of_flights = no_of_flights
        self.exact_covers = []

    @staticmethod
    def flatten(list_of_routes):
        flat_list = []
        for route in list_of_routes:
            flat_list += route
        return flat_list

    def check_size(self, flat_list):
        if len(flat_list) == self.no_of_flights:
            return True
        else:
            return False

    @staticmethod
    def check_unique_flights(flat_list):
        counter = Counter(flat_list)
        for values in counter.values():
            if values > 1:
                return False
        return True

    def generate_exact_cover(self):
        self.route_combinations = itertools.combinations(self.routes, self.size_of_fleet)
        for comb in self.route_combinations:
            flat_list = self.flatten(comb)
            if self.check_size(flat_list) and self.check_unique_flights(flat_list):
                self.exact_covers.append(comb)
