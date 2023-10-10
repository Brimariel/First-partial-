# Ask user for input
price = float(input("Enter the price of the product: "))
category = input("Enter the category of the product (A, B, or C): ")
units = int(input("Enter the number of units purchased: "))

# Define discount percentages based on category
discount_a = 0.10  # 10% discount for category A
discount_b = 0.05  # 5% discount for category B
discount_c = 0.02  # 2% discount for category C
additional_discount = 0.05  # Additional 5% discount for more than 10 units

# Apply category discount
if category.upper() == 'A':
    discount = discount_a
elif category.upper() == 'B':
    discount = discount_b
elif category.upper() == 'C':
    discount = discount_c
else:
    print("Invalid category.")
    exit()

# Apply additional discount for more than 10 units
if units > 10:
    discount += additional_discount

# Calculate final price after discounts
discounted_price = price - (price * discount * units)

# Display the final price
print(f"The final price after all discounts is: ${discounted_price:.2f}")
---------------------------------------------------------------------------------------------------------

# Ask user for input
weight_kg = float(input("Enter your weight in kilograms: "))
duration_minutes = float(input("Enter the duration of the activity in minutes: "))
activity = input("Enter the type of activity (running, swimming, cycling): ")

# Constants (calories burned per minute per kilogram for different activities)
calories_burned_per_minute_running = 11.4
calories_burned_per_minute_swimming = 9.7
calories_burned_per_minute_cycling = 8.4

# Calculate total calories burned based on activity type
if activity.lower() == "running":
    calories_burned = calories_burned_per_minute_running * duration_minutes * weight_kg
elif activity.lower() == "swimming":
    calories_burned = calories_burned_per_minute_swimming * duration_minutes * weight_kg
elif activity.lower() == "cycling":
    calories_burned = calories_burned_per_minute_cycling * duration_minutes * weight_kg
else:
    print("Invalid activity type.")
    exit()

# Display the total calories burned
print(f"You burned {calories_burned:.2f} calories during {duration_minutes} minutes of {activity}.")
----------------------------------------------------------------------------------------------------------------

# Get user input for distance in miles and car's miles per gallon (MPG)
distance = float(input("Enter the distance of your trip in miles: "))
mpg = float(input("Enter your car's miles per gallon (MPG): "))

# Get user input for current price of gasoline per gallon and number of days for the trip
gas_price = float(input("Enter the current price of gasoline per gallon: $"))
days = int(input("Enter how many days you plan to travel: "))

# Calculate total number of gallons needed for the trip
gallons_needed = distance / mpg

# Calculate total cost of the trip considering changing gasoline prices during the journey
total_cost = gallons_needed * gas_price

# Display the total cost of the trip
print(f"Total cost of the trip: ${total_cost:.2f}")

# Calculate daily cost considering changing gasoline prices
daily_cost = total_cost / days
print(f"Estimated daily cost: ${daily_cost:.2f}")
