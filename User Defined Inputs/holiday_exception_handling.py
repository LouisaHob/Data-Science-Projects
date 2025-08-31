"""
This program calculates a user's total holiday cost, 
including flight, hotel, and car rental costs.
It uses functions to calculate the costs based on user 
input and provides options for different cities.
It includes a menu-driven program to interactively
calculate holiday cost based on user input.
Prices for flights and hotels are stored in dictionaries, 
and the car rental cost is calculated based on a fixed daily rate.

This program includes exception handling to make it more user 
friendly and robust.
"""

# Functions that calculate the cost of flights, hotels, and car rentals
def city_options():
    print("\n")
    print("Options:")
    print("m = Milan")
    print("r = Rome")
    print("p = Paris")
    print("l = London")
    print("\n")

def get_city_choice():
    while True:  # Keep looping until a valid input is received
        city_options()
        choice = input("Enter the letter of the city you want to fly to: ").lower()
        if choice == "m":
            return "Milan"
        elif choice == "r":
            return "Rome"
        elif choice == "p":
            return "Paris"
        elif choice == "l":
            return "London"
        else:
            print("Invalid choice. Please try again.")

def flight_cost(city):
    return flight_price_dict[city]

def hotel_cost(city, num_nights):
    return hotel_price_dict[city] * num_nights

def car_rental(rental_days, price=30):
    return price * rental_days

def holiday_cost(flight_total, hotel_total, car_total):
    return flight_total + hotel_total + car_total

# Flight prices for different cities
flight_price_dict = {'Milan': 120,
                     'Rome': 130,
                     'Paris': 140,
                     'London': 150
                     }

# Hotel prices for different cities
hotel_price_dict = {'Milan': 104,
                     'Rome': 163,
                     'Paris': 222,
                     'London': 217
                     }

# Get user input for city, number of nights, and rental days

city = get_city_choice()

# Flight cost
flight_total = flight_cost(city)

# Exception handling for hotel stay (ensures valid input)
while True:
    try:
        num_nights = int(input("Enter the number of nights you want to stay: "))
        if num_nights <= 0:
            print("Please enter a positive number of nights.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number of nights.")

hotel_total = hotel_cost(city, num_nights)

# Exception handling for car rental (ensures valid input)
while True:
    try:
        rental_days = int(input("Enter the number of days you want to hire a car: "))
        if rental_days <= 0:
            print("Please enter a positive number of rental days.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number of rental days.")

car_total = car_rental(rental_days)

# Calculate total holiday cost
holiday_total = holiday_cost(flight_total, hotel_total, car_total)

# Print statements 
print("\n")
print(f"------------Holiday Cost to {city} Summary------------")
print(f"Flight cost: £{flight_total}")
print(f"Hotel cost for {num_nights} nights: £{hotel_total}")
print(f"Car rental for {rental_days} days: £{car_total}")
print("\n")
print(f"Total holiday cost: £{holiday_total}")
print("-----------------------------------------------------")