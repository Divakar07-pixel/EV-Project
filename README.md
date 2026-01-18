# ⚡ EV Charging Booking System

A simple Python desktop application that allows users to **book electric vehicle charging slots** at predefined stations. Built using **Tkinter GUI** and **SQLite database**, this project demonstrates backend logic, SQL usage, and basic UI integration — ideal for learners and early-career developers.

---

## 🚀 Features

- 📍 View and store available charging stations  
- 👤 Book charging slots with customer name, vehicle model, desired time, and station selection  
- 📅 Check slot availability before booking  
- 🗄️ Use SQLite for structured persistent data storage  
- 🧠 Enforced SQL logic to avoid double bookings

---

## 🧩 Motivation

This project was created to practice and improve **SQL skills**, especially:

- Table design with foreign key relationships  
- Querying for availability checks  
- Inserting records with validation  
- Simple database interaction integrated with a UI  

It’s a beginner-friendly project that focuses more on SQL and backend logic than on advanced UI features.

---

## 📦 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Tkinter | Desktop GUI framework |
| SQLite | Local database storage |
| SQL | Backend logic and query execution |

---

## 🗃️ Database Schema

### `charging_stations`

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER PK | Unique station ID |
| name | TEXT | Station name |
| location | TEXT | Station location |

### `bookings`

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER PK | Unique booking ID |
| customer_name | TEXT | Customer’s full name |
| vehicle_model | TEXT | EV model name |
| charging_time | TEXT | Time of desired charging |
| station_id | INTEGER | Foreign key to `charging_stations.id` |

SQLite automatically creates the database file (`ev_charging.db`) upon running the application.

---

## 📥 Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Divakar07-pixel/EV-Project.git
