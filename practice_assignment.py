# Simple activity registration with basic input/output
print("Welcome to Karmu High School Activity Registration!")
# Get student info
name = input("Enter your name: ")
age = input("Enter your age: ")
# Show activities
print("\nChoose an activity:")
print("1. Music Jam Session (2 hours, easy, $5)")
print("2. Science Experiments Lab (3 hours, moderate, $10)")
print("3. Sports Leadership Training (4 hours, challenging, $12)")
# Get activity choice
choice = input("Enter activity number (1-3): ")
# Set activity details
if choice == "1":
    activity = "Music Jam Session"
    cost = 5
elif choice == "2":
    activity = "Science Experiments Lab"
    cost = 10
else:
    activity = "Sports Leadership Training"
    cost = 12
   # Get meal choice
print("\nMeal options:")
print("1. Standard")
print("2. Vegetarian")
print("3. Dairy-free")
print("4. No meal")
meal = input("Enter meal number (1-4): ")
 # Set meal details
if meal == "1":
    meal_type = "standard"
elif meal == "2":
    meal_type = "vegetarian"
elif meal == "3":
    meal_type = "dairy-free"
else:
    meal_type = "no meal"
# Show summary
print(f"\n{name}, age {age}, chose {activity}, meal: {meal_type}. Total: ${cost}")
