class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receit(self):
        print(f"Receit\nDistance: {self.distance}\nFare: {self.fare}\n//////////////////\nRate: {self.rate_per_km}")


def main():
    ride1 = TaxiRide(7)
    ride2 = TaxiRide(4.25)
    ride1.calculate_fare(15)
    ride2.calculate_fare(21)
    ride1.print_receit()
    ride2.print_receit()

if __name__ == "__main__":
    main()
