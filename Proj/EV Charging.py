import sqlite3
import random
from datetime import datetime, timedelta
from flask import Flask, request, redirect, url_for, render_template, jsonify

app = Flask(__name__)

DB_NAME = "ev_network.db"

# ---------------- DB HELPER ----------------
def get_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

# ---------------- CREATE TABLES ----------------
def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stations (
        station_id TEXT PRIMARY KEY,
        location_name TEXT,
        city TEXT,
        country TEXT,
        latitude REAL,
        longitude REAL,
        charger_type TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS charging_sessions (
        session_id TEXT PRIMARY KEY,
        station_id TEXT,
        start_time TEXT,
        end_time TEXT,
        kwh_consumed REAL,
        total_cost REAL,
        payment_status TEXT
    )
    """)

    conn.commit()
    conn.close()

# ---------------- MOCK DATA ----------------
def seed_data():
    conn = get_db()
    cursor = conn.cursor()

    cities = [
        ("T Nagar Mall", "Chennai", "India", 13.08, 80.27),
        ("Mumbai Central", "Mumbai", "India", 19.07, 72.87),
        ("Delhi Metro", "Delhi", "India", 28.70, 77.10),
        ("Tech Park", "Bangalore", "India", 12.97, 77.59),
        ("Downtown Hub", "New York", "USA", 40.71, -74.00),
        ("Westside Mall", "Los Angeles", "USA", 34.05, -118.24)
    ]

    for i, c in enumerate(cities):
        cursor.execute("""
        INSERT OR IGNORE INTO stations VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            f"ST-{100+i}",
            c[0],
            c[1],
            c[2],
            c[3],
            c[4],
            random.choice(["Level 2", "DC Fast"])
        ))

    conn.commit()
    conn.close()

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    search = request.args.get("search")
    search_type = request.args.get("search_type", "city")

    conn = get_db()
    cursor = conn.cursor()

    if search:
        cursor.execute(
            f"SELECT * FROM stations WHERE {search_type} LIKE ?",
            ('%' + search + '%',)
        )
    else:
        cursor.execute("SELECT * FROM stations")

    stations = cursor.fetchall()
    conn.close()

    return render_template(
        "index.html",
        stations=stations,
        total=len(stations),
        india=len([s for s in stations if s[3] == "India"]),
        usa=len([s for s in stations if s[3] == "USA"]),
        fast=len([s for s in stations if s[6] == "DC Fast"])
    )

@app.route("/add_station", methods=["POST"])
def add_station():
    data = request.form
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        f"ST-{random.randint(1000,9999)}",
        data["location_name"],
        data["city"],
        data["country"],
        data["latitude"],
        data["longitude"],
        data["charger_type"]
    ))

    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/autocomplete")
def autocomplete():
    q = request.args.get("q", "")
    t = request.args.get("type", "city")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT {t} FROM stations WHERE {t} LIKE ?", (q+"%",))
    results = [r[0] for r in cursor.fetchall()]
    conn.close()

    return jsonify(results)

# ---------------- MAIN ----------------
if __name__ == "__main__":
    init_db()
    seed_data()
    app.run(debug=True)