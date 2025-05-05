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

