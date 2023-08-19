from InstanceGenerator import InstanceGenerator
from Knuth import Knuth


if __name__ == '__main__':
    instance = InstanceGenerator(no_of_flights=20, no_of_ports=10, no_of_aircrafts=8)
    # for i in instance.flights:
    #     print(i.flight_id, i.origin_port, i.dest_port, i.departure_timestamp, i.arrival_timestamp)
    print(instance.routes)
    print("---------------------------------------------")
    knuth = Knuth(instance.no_of_aircrafts, instance.routes, instance.no_of_flights)
    knuth.generate_exact_cover()
    for i in instance.routes:
        print(i)
    print("---------------------------------------------")
    for i in knuth.exact_covers:
        print(i)
    print(len(knuth.exact_covers))
