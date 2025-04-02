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