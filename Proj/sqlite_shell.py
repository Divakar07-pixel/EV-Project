import sqlite3

def main():
    conn = sqlite3.connect('ev_network.db')
    cursor = conn.cursor()

    print("Connected to ev_network.db")
    print("Type your SQL queries. Type 'exit' to quit.")

    while True:
        query = input("sqlite> ")
        if query.lower() == 'exit':
            break
        try:
            cursor.execute(query)
            if query.strip().upper().startswith('SELECT'):
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                conn.commit()
                print("Query executed.")
        except Exception as e:
            print(f"Error: {e}")

    conn.close()
    print("Disconnected from database.")

if __name__ == '__main__':
    main()
