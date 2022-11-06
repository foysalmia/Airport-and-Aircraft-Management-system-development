import csv
from airport import Airport


class AllAirports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airports.csv')

    def load_airport_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        # get currency name to relate with rate
        with open('./data/curancyrates.csv', 'r') as curRate:
            lines = csv.reader(curRate)
            for line in lines:
                currency_rates[line[1]] = line[2]
        curRate.close()

        # dictionary country to ralate
        with open('./data/countrycurancy.csv', 'r') as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()

        # create airport
        with open(file_path, 'r', encoding='utf8') as files:
            lines = csv.reader(files)

            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(
                        line[4], line[1], line[2], line[3], line[6], line[7], rate)
            except:
                print("there is a key error")

            self.airports = airports
        files.close()

        for airport in airports.items():
            print(airport)


AllAirports()
