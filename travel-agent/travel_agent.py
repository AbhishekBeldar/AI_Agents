
class TravelAgent:
    def __init__(self):
        self.memory = {
            "previous_destinations": [],
            "preferences": []
        }

    # Tool 1: Weather
    def get_weather(self, destination):
        weather_data = {
            "Chikmagalur": "Pleasant with possible rain",
            "Mysuru": "Sunny",
            "Coorg": "Cloudy with possible rain",
            "Bengaluru": "Partly cloudy"
        }

        return weather_data.get(
            destination,
            "Weather information unavailable"
        )

    # Tool 2: Places
    def find_places(self, destination):
        places = {
            "Chikmagalur": [
                "Mullayanagiri",
                "Baba Budangiri",
                "Jhari Falls"
            ],
            "Mysuru": [
                "Mysore Palace",
                "Mysore Zoo",
                "Chamundeshwari Temple"
            ],
            "Coorg": [
                "Abbey Falls",
                "Raja's Seat",
                "Dubare"
            ],
            "Bengaluru": [
                "Lalbagh Botanical Garden",
                "Bangalore Palace",
                "Cubbon Park"
            ]
        }

        # Allow common capitalization differences.
        matching_destination = next(
            (
                name for name in places
                if name.casefold() == destination.strip().casefold()
            ),
            None
        )

        return places.get(matching_destination, [])

    # Tool 3: Estimate budget
    def estimate_budget(self, days, people):
        daily_cost = 1500
        return days * people * daily_cost

    # Memory
    def save_memory(self, destination):
        self.memory["previous_destinations"].append(destination)

    # Planning
    def create_plan(self, destination, days, people):
        destination = destination.strip()

        if not destination:
            return "Please enter a destination."

        if not isinstance(days, int) or not 1 <= days <= 30:
            return "Days must be between 1 and 30."

        if not isinstance(people, int) or not 1 <= people <= 20:
            return "People must be between 1 and 20."

        weather = self.get_weather(destination)
        places = self.find_places(destination)
        budget = self.estimate_budget(days, people)

        if not places:
            return (
                "Unable to create itinerary for this destination. "
                "Try Chikmagalur, Mysuru, Coorg, or Bengaluru."
            )

        itinerary = {
            "destination": destination,
            "days": days,
            "people": people,
            "weather": weather,
            "places": places[:days],
            "estimated_budget": budget
        }

        self.save_memory(destination)

        return itinerary


# Run the original terminal program only when this file
# is executed directly, not when another Python file imports it.
if __name__ == "__main__":
    agent = TravelAgent()

    destination = input("Enter destination: ")

    try:
        days = int(input("Enter number of days: "))
        people = int(input("Enter number of people: "))

        result = agent.create_plan(destination, days, people)

        print("\n----- TRAVEL PLAN -----")

        if isinstance(result, dict):
            print("Destination:", result["destination"])
            print("Duration:", result["days"], "days")
            print("People:", result["people"])
            print("Weather:", result["weather"])

            print("\nPlaces to Visit:")
            for place in result["places"]:
                print("-", place)

            print(
                "\nEstimated Budget: ₹",
                result["estimated_budget"]
            )
        else:
            print(result)

    except ValueError:
        print("Please enter valid whole numbers for days and people.")
