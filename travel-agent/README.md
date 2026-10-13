
# TravelMate - Mini Autonomous Travel Agent

## About the Project

TravelMate is a Python-based travel planning application. Users can select a destination, enter the number of days and travellers, and receive a basic itinerary with weather information, suggested attractions, and an estimated budget.

## Features

- Destination-based travel planning
- Suggested tourist attractions
- Basic weather information
- Estimated trip budget
- Input validation
- Browser-based frontend
- Flask backend API

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Supported Destinations

- Chikmagalur
- Mysuru
- Coorg
- Bengaluru

## How to Run

1. Open a terminal in the `travel-agent` folder.
2. Install dependencies:

   `python -m pip install -r requirements.txt`

3. Start the application:

   `python -m backend.app`

4. Open `http://127.0.0.1:5000` in your browser.

## Budget Calculation

The application estimates the budget using:

`Number of days × Number of people × ₹1,500`

This is a sample estimate, not a live travel price.

## Limitations

Weather information and attractions are stored in predefined Python dictionaries. The application does not currently use live weather services, maps, hotel booking systems, or live prices.

## Future Improvements

- Integrate a live weather API
- Add hotel and transport recommendations
- Add maps and route planning
- Save user preferences and trip history
