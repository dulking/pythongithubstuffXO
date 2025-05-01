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

