from Flight import Flight
import random


class InstanceGenerator:
    def __init__(self, no_of_flights, no_of_ports, no_of_aircrafts):
        self.no_of_aircrafts = no_of_aircrafts
        self.no_of_flights = no_of_flights
        self.no_of_ports = no_of_ports
        self.flights = []
        self.routes = []
        self.distance_matrix = []
        self.exact_cover_representation = []
        self.generate_distance_matrix()
        self.generate_tap()
        self.generate_routes()

    def generate_distance_matrix(self):
        for i in range(self.no_of_ports):
            self.distance_matrix.append([])
            for j in range(self.no_of_ports):
                if i == j:
                    self.distance_matrix[i].append(0)   # same airports = 0
                elif j > i:
                    self.distance_matrix[i].append(random.randint(1, 12))   # randomize first half of matrix
                else:
                    self.distance_matrix[i].append(self.distance_matrix[j][i])  # copy values from corresponding cells

    def avoid_duplicate_ports(self, origin_port):
        destination_port = random.randint(1, self.no_of_ports)
        while origin_port == destination_port:
            destination_port = random.randint(1, self.no_of_ports)
        return destination_port

    def generate_tap(self):
        for f_no in range(self.no_of_flights):
            flight_id = f_no + 1
            origin_port = random.randint(1, self.no_of_ports)
            destination_port = self.avoid_duplicate_ports(origin_port)
            departure_timestamp = random.randint(0, 24)
            arrival_timestamp = self.distance_matrix[origin_port - 1][destination_port - 1] + departure_timestamp   # values above 24 mean one day ahead
            self.flights.append(Flight(flight_id, origin_port, destination_port, departure_timestamp, arrival_timestamp))

    def find_flight_by_id(self, f_id):
        for f in self.flights:
            if f.flight_id == f_id:
                return f

    def find_new_flight(self, route):
        last_flight = self.find_flight_by_id(route[-1])
        if last_flight is not None:
            last_port = last_flight.dest_port
            last_arrival = last_flight.arrival_timestamp
            for f in self.flights:
                if f.flight_id not in route and last_port == f.origin_port and last_arrival <= f.departure_timestamp:   # same airport, departure after (or the same as) arrival
                    return f.flight_id

    def add_flights_to_routes(self, base_layer, current_layer):
        if not base_layer:
            for f in self.flights:
                current_layer.append([f.flight_id])
        else:
            for r in base_layer:
                new_flight = self.find_new_flight(r)
                if new_flight is not None:
                    new_route = r.copy()
                    new_route.append(new_flight)
                    current_layer.append(new_route)

    def generate_routes(self):
        routes = []
        base_layer = []
        current_layer = []

        for size in range(self.no_of_flights):
            self.add_flights_to_routes(base_layer, current_layer)
            if current_layer:
                new_routes = current_layer.copy()
                routes.extend(new_routes)
                base_layer = [i for i in current_layer]
                current_layer.clear()
            else:
                break
        self.routes = [i for i in routes]
