"""
#School Holiday Camp Registration Program
 # Author: [Your Name]
 # Date: [Current Date]

This program allows campers to register for various holiday camp options,
select their preferences, and receive a cost summary and confirmation.
"""
# Constants for camp options
CAMPS = {
    "1": {
        "name": "Cultural immersion",
        "days": 5,
        "difficulty": "easy",
        "base_cost": 800
    },
    "2": {
        "name": "Kayaking and pancakes",
        "days": 3,
        "difficulty": "moderate",
        "base_cost": 400
    },
    "3": {
        "name": "Mountain biking",
        "days": 4,
        "difficulty": "difficult",
        "base_cost": 900
    }
}
# Meal options and costs
MEALS = {
    "1": {"name": "No meals", "cost": 0},
    "2": {"name": "Lunch only", "cost": 50},
    "3": {"name": "Full board (breakfast, lunch, dinner)", "cost": 100}
}
def get_valid_input(prompt, input_type=str, valid_options=None, min_value=None, max_value=None):
    """
    Helper function to get valid input from user with error handling
    Parameters:
        prompt (str): The message to display to the user
        input_type (type): The expected type of input (str, int, etc.)
        valid_options (list/dict): Optional list of valid choices
        min_value: Minimum allowed value (for numeric inputs)
        max_value: Maximum allowed value (for numeric inputs)
    
    Returns:
        The validated user input
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty")
  



