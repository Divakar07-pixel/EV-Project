# EV Charging Booking System

A simple Python application for booking electric vehicle charging slots at various stations.

## Features

- View available charging stations
- Book charging slots with customer details
- Check slot availability
- SQLite database for data storage

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Divakar07-pixel/EV-Project.git
   cd EV-Project
   ```

2. Run the application:
   ```
   python Front
   ```

## Usage

1. Enter your name, vehicle model, desired charging time, and station ID
2. Click "Book Charging Slot" to make a reservation
3. The system will confirm if the slot is available or show an error if booked

## Database

The application uses SQLite database `ev_charging.db` with two tables:
- `charging_stations`: Station information
- `bookings`: Customer booking records

## Contributing

Feel free to submit issues and pull requests.

## License

This project is open source.