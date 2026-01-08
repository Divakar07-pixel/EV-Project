# Autocomplete Feature for Indian Cities
# This program provides an autocomplete feature for Indian cities.
# It accepts user input from the terminal and displays matching city names that start with the entered characters.
# The search is case-insensitive, and the program continues until the user types 'exit'.

# List of major Indian cities (you can expand this list as needed)
indian_cities = [
    "Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Indore", "Jaipur", "Kolkata",
    "Lucknow", "Mumbai", "Nagpur", "Pune", "Surat", "Thane", "Vadodara", "Visakhapatnam",
    "Agra", "Ajmer", "Aligarh", "Allahabad", "Amritsar", "Aurangabad", "Bareilly", "Bhubaneswar",
    "Bhopal", "Chandigarh", "Coimbatore", "Cuttack", "Dehradun", "Dhanbad", "Faridabad",
    "Ghaziabad", "Gorakhpur", "Gurgaon", "Guwahati", "Gwalior", "Hubli-Dharwad", "Jabalpur",
    "Jalandhar", "Jammu", "Jamshedpur", "Jhansi", "Jodhpur", "Kakinada", "Kanpur", "Kochi",
    "Kozhikode", "Ludhiana", "Madurai", "Mangalore", "Meerut", "Moradabad", "Mysore",
    "Nashik", "Navi Mumbai", "Noida", "Patiala", "Patna", "Pondicherry", "Raipur", "Rajkot",
    "Ranchi", "Rourkela", "Salem", "Sangli", "Shimla", "Siliguri", "Solapur", "Srinagar",
    "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Trivandrum", "Udaipur", "Ujjain", "Vijayawada",
    "Warangal", "Yamunanagar"
]

def main():
    print("Welcome to Indian Cities Autocomplete!")
    print("Type one or more characters to search for cities starting with those letters.")
    print("Type 'exit' to quit the program.")
    print("Country: India\n")

    while True:
        # Get user input
        user_input = input("Enter search term: ").strip()

        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # If input is empty, skip
        if not user_input:
            print("Please enter at least one character.\n")
            continue

        # Find matching cities (case-insensitive)
        matching_cities = [
            city for city in indian_cities
            if city.lower().startswith(user_input.lower())
        ]

        # Display results
        if matching_cities:
            print(f"\nFound {len(matching_cities)} matching cities in India:")
            for city in sorted(matching_cities):  # Sort for clean output
                print(f"  - {city}, India")
        else:
            print(f"\nNo cities found starting with '{user_input}' in India.")

        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()
