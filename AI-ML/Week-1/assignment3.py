# Functions
"""
 The Challenge: Build a POS Receipt GeneratorBackground Scenario:

You are writing software for a store checkout terminal. The terminal needs to calculate the final price 
of an item after applying an optional membership discount and local sales tax. Finally, it must print a 
perfectly aligned line for the paper receipt.

Your Task:
Write a Python function named create_receipt_line(item_name, price) that contains two
nested (inner) functions:

1-apply_discount(current_price):
An inner function that takes the current price, subtracts a 15% membership discount, and returns the new price.

2-apply_tax(current_price):
An inner function that takes the discounted price, adds a 7% sales tax, and returns the final total.


def create_receipt_line(item_name, price ):
    
    def apply_discount(current_price):
        saving = current_price * (15 / 100)
        new_price = current_price - saving
        return new_price
    

    def apply_tax(current_price):
        tax_amount = current_price * (7 / 100)
        final_total = current_price + tax_amount
        return final_total
    
    discounted_price = apply_discount(price)
    final_total = apply_tax(discounted_price)
    print(f"Receipt: {item_name} | total_price: {final_total}")

create_receipt_line("Leather Boots", 120.00)
create_receipt_line("Gaming Laptop", 1500.00)

"""

"""

 The Challenge: The Movie Ticket Booking SystemBackground Scenario
 
 You are designing the backend function for a cinema ticketing kiosk. The kiosk needs to compute the 
 total ticket bill based on the age of the customer and whether they want to upgrade their ticket to 
 a 3D/IMAX experience.
 
 Your Task:
 
 Write a main function called book_ticket(movie_name, base_price, age) that contains two nested (inner) functions:
 
 1-get_age_multiplier(age):
 
 Takes the customer's age and returns a decimal pricing multiplier based on these store rules:
    1-Children (under 12) get a 50% discount (multiplier: 0.5)
    2-Seniors (65 and older) get a 30% discount (multiplier: 0.7)
    3-Everyone else pays full price (multiplier: 1.0)
    
2-add_experience_upgrades(current_price):
    1-Takes the age-adjusted ticket price.
    2-If a global variable named IS_3D is set to True, it adds a flat premium charge of $5.00 to
      the ticket. Otherwise, it adds nothing.

"""

IS_3D = True

def book_ticket(movie_name, base_price, age):
    def get_age_multipler(age):
        if age < 12:
            return base_price * (50 / 100)
        elif age >= 65:
            return base_price * (30 / 100)
        else:
            return base_price

    def add_experience_upgrades(current_price):
        if IS_3D:
            return current_price + 5.00 
        else:
            return current_price
    adjusted_age = get_age_multipler(age)
    final_total = add_experience_upgrades(adjusted_age)
    print(f"{movie_name}: | Total_Price: ${final_total}")

book_ticket("Avatar 3", 14.00, 10)
book_ticket("The Avengers", 14.00, 28)