"""
School Holiday Camp Registration Program
Author: [Your Name]
Date: [Current Date]

This program manages registrations for a school holiday camp with:
- Multiple camp options
- Meal plan choices
- Transportation option
- Registration data storage
"""

# Camp data stored in a list of dictionaries
CAMPS = [
    {
        "code": "1",
        "name": "Cultural immersion",
        "duration": 5,
        "difficulty": "easy",
        "base_cost": 800
    },
    {
        "code": "2",
        "name": "Kayaking and pancakes",
        "duration": 3,
        "difficulty": "moderate",
        "base_cost": 400
    },
    {
        "code": "3",
        "name": "Mountain biking",
        "duration": 4,
        "difficulty": "difficult",
        "base_cost": 900
    }
]

# Meal options stored in a list of dictionaries
MEAL_PLANS = [
    {
        "code": "1",
        "description": "No meals",
        "daily_cost": 0
    },
    {
        "code": "2",
        "description": "Lunch only",
        "daily_cost": 50
    },
    {
        "code": "3",
        "description": "Full board (breakfast, lunch, dinner)",
        "daily_cost": 100
    }
]

# Transportation cost constant
TRANSPORT_COST = 80

# List to store all registrations
all_registrations = []

def display_options(options, title):
    """
    Display available options with a title
    
    Args:
        options (list): List of option dictionaries
        title (str): Display title for the options
    """
    print(f"\n{title}:")
    for option in options:
        print(f"{option['code']}. {option.get('name', option.get('description'))}")

def get_valid_choice(options, prompt):
    """
    Get and validate user choice from available options
    
    Args:
        options (list): Available options
        prompt (str): Input prompt to display
    
    Returns:
        str: Validated choice code
    """
    valid_codes = [option["code"] for option in options]
    
    while True:
        choice = input(prompt).strip()
        if choice in valid_codes:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(valid_codes)}")


def get_yes_no(prompt):
    """
    Get yes/no input from user
    
    Args:
        prompt (str): Question to ask user
    
    Returns:
        bool: True for yes, False for no
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        print("Please answer 'yes' or 'no'.")

def calculate_total_cost(camp, meal_plan, needs_transport):
    """
    Calculate total cost for registration
    
    Args:
        camp (dict): Selected camp details
        meal_plan (dict): Selected meal plan
        needs_transport (bool): Whether transport is needed
    
    Returns:
        int: Total calculated cost
    """
    base_cost = camp["base_cost"]
    meal_cost = meal_plan["daily_cost"] * camp["duration"]
    transport_cost = TRANSPORT_COST if needs_transport else 0
    return base_cost + meal_cost + transport_cost
def register_camper():
    """Register a new camper and return registration details"""
    print("\n--- New Registration ---")
   # Get camper information
    while True:
        camper_name = input("Enter camper's name: ").strip()
        if camper_name:
            break
        print("Name cannot be empty. Please try again.")
    
    while True:
        try:
            camper_age = int(input("Enter camper's age (5-17): ").strip())
            if 5 <= camper_age <= 17:
                break
            print("Age must be between 5 and 17.")
        except ValueError:
            print("Please enter a valid number for age.")
 # Select camp
    display_options(CAMPS, "Available Camps")
    camp_choice = get_valid_choice(CAMPS, "Select camp (1-3): ")
    selected_camp = next(camp for camp in CAMPS if camp["code"] == camp_choice)
    
# Select meal plan
    display_options(MEAL_PLANS, "Meal Plan Options")
    meal_choice = get_valid_choice(MEAL_PLANS, "Select meal plan (1-3): ")
    selected_meal = next(meal for meal in MEAL_PLANS if meal["code"] == meal_choice)
    
 # Transportation option
    needs_transport = get_yes_no("Do you need transportation to camp? (yes/no): ")
  # Calculate total cost
    total_cost = calculate_total_cost(selected_camp, selected_meal, needs_transport)
  # Create registration record
    registration = {
        "name": camper_name,
        "age": camper_age,
        "camp": selected_camp["name"],
        "duration": selected_camp["duration"],
        "difficulty": selected_camp["difficulty"],
        "meal_plan": selected_meal["description"],
        "transportation": "Yes" if needs_transport else "No",
        "total_cost": total_cost,
        "confirmed": False
    }
   # Display summary
    print("\n--- Registration Summary ---")
    for key, value in registration.items():
        if key != "confirmed":
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Confirm registration
    if get_yes_no("\nConfirm registration? (yes/no): "):
        registration["confirmed"] = True
        print("\nRegistration confirmed! Thank you.")
        return registration
    
    print("\nRegistration cancelled.")
    return None

def main():
    """Main program function"""
    print("Welcome to Tane's School Holiday Camp Registration!")
    print("--------------------------------------------------")
    
    # Main program loop
    while True:
        # Register new camper
        registration = register_camper()
        if registration and registration["confirmed"]:
            all_registrations.append(registration)
       
        # Ask if you want to register another camper
        if not get_yes_no("\nRegister another camper? (yes/no): "):
            break
     
    # Display all confirmed registrations
    if all_registrations:
        print("\n--- All Confirmed Registrations ---")
        for i, reg in enumerate(all_registrations, 1):
            print(f"\nRegistration #{i}:")
            for key, value in reg.items():
                if key != "confirmed":
                    print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("\nNo registrations were confirmed.")
    
    print("\nThank you for using the registration system!")

if __name__ == "__main__":
    main()
    

    



 

    
