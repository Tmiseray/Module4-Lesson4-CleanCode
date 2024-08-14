# Weather Forecast Application Refactored

class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city

    # fetch data for given city
    def retrieve_data(self):
        print(f"\nRetrieving Weather Data for {self.city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})

class DataParser:
    # Parse Weather Data
    def parse_weather_data(self, data, detailed):
        if not data:
            return "\nWeather data not available."
        else:
            city = data['city']
            temperature = data['temperature']
            condition = data['condition']
            humidity = data['humidity']
            if detailed == 'yes':
                return f"\nWeather in {city}:\n- Temperature: {temperature} degrees\n- Condition: {condition}\n- Humidity: {humidity}%"
            else:
                return f"\nWeather in {city}:\n- Temperature: {temperature} degrees"

class UserInterface:
    def __init__(self):
        self.parser = DataParser()

    # What user sees/interacts with
    def retrieve_forecast(self):
        print("\n.~* Retrieve Forecast *~.\n")
        city = input("Enter the city: ")
        detailed = input("\nDo you want a detailed forecast? (yes/no): ")
        self.data_fetcher = WeatherDataFetcher(city)
        data = self.data_fetcher.retrieve_data()
        return self.parser.parse_weather_data(data, detailed)

    def menu(self):
        while True:
            menu = "~* MENU *~"
            print("\n.~* Weather Forecast Application *~.\n")
            print(f"{menu.center(28, '.')}")
            print("1. Retrieve Weather Forecast")
            print("2. Exit")
            choice = input("Enter your choice (1/2): ")
            try:
                if choice == '2':
                    print("\nThank you for using Weather Forecast Application!")
                    print("Exiting program...")
                    break
                elif choice == '1':
                    forecast = self.retrieve_forecast()
                    print(forecast)
                else:
                    print("\nInvalid choice. Please try again.")
            except Exception as e:
                print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    ui = UserInterface()
    ui.menu()