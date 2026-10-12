# varible and Data types
# Employee Profile
# Task 1
name  = "Ali Hassan"
age = 26
salary = 50000
dept = "information technology"
currenlty_employed = True

print("Employee name is ", name)
print("Empolyee age is ", age)
print("Empolyee salary is ", float(salary))
print("Empolyee is employed ", currenlty_employed)

print(type(name))
print(type(age))
print(type(salary))
print(type(dept))
print(type(currenlty_employed))

# Task 2
# Product Information

product_name = "Phone"
product_id = 12345
product_price = 30000
product_quantity = 3
inventory_value = product_price * product_quantity

print("Product name is ", product_name)
print("Product ID is ", product_id)
print("Product price is ", float(product_price))
print("Product quantity is ", product_quantity)
print("Inventory value is ", inventory_value)

# Operators
# Task 1
# Number Calulator

a =  10
b = 3

print("Addition of two numbers is ", a + b)
print("Subtraction of two numbers is ", a - b)
print("Multiplication of two numbers is ", a * b)
print("Division of two numbers is ", a / b)
print("Floor division of two numbers is ", a // b)
print("Modulus of two numbers is ", a % b)
print("Exponentiation of two numbers is ", a ** b)


# Task 2
# Rectangle Area and Perimeter Calculator

Lenght = 5
Width = 3
area = Lenght * Width
primeter = 2 * (Lenght + Width)
length_squ = Lenght ** 2
width_squ = Width ** 2

print("Area of rectangle is ", area)
print("Perimeter of rectangle is ", primeter)
print("Length squared is ", length_squ)
print("Width squared is ", width_squ)

# String and String Operations
# Task 1
# Name Formatter

name = input("Enter your name:")

print("Orignal name is ", name)
print("Uppercase name is ", name.upper())
print("Lowercase name is ", name.lower())
print("Length of name is ", len(name))
print("First character of name is ", name[0])
print("Last character of name is ", name[-1])
print("First three characters of name is ", name[0:3])
print("Last three characters of name is ", name[-3:])

# Task 2
# Email Analyzer

email = input("Enter your email address:")
username = email.split("@")[0]
domain = email.split("@")[1]

print("Orignal email is ", email)
print("Username is ", username)
print("Domain is ", domain)
print("Length of email is ", len(email))

# Input and Type casting
# Task 1
# ATM Withdrawal Calculator

name = input("Enter your account holder name:")
current_balance = float(input("Enter your current balance:"))
withdrawal_amount = float(input("Enter the amount you want to withdraw:"))
note_recieced = int(input("Enter the number of notes received:"))
remaining_balance = current_balance - withdrawal_amount
amount_per_note = withdrawal_amount / note_recieced

print("Account holder name is ", name)
print("Current balance is ", current_balance)
print("Withdrawal amount is ", withdrawal_amount)
print("Reamaining balance is ", remaining_balance)
print("Amount per note is ", amount_per_note)

# Task 2
# Movie Ticket Calculator

customer_name = input("Enter Customer name:")
adult_tickets = int(input("Enter number of adult tickets:"))
adult_ticket_price = float(input("Enter price of adult ticket:"))
child_tickets = int(input("Enter number of child tickets:"))
child_ticket_price = float(input("Enter price of child ticket:"))
popcorn_quantity = int(input("Enter quantity of popcorn:"))
popcorn_price = float(input("Enter price of popcorn:"))

adult_total = adult_tickets * adult_ticket_price
child_total = child_tickets * child_ticket_price
popcorn_total = popcorn_quantity * popcorn_price
total_amount = adult_total + child_total + popcorn_total

print("Customer name is ", customer_name)
print("Total amount for adult tickets is ", adult_total)
print("total amount for adult tickets is ", adult_total)
print("Total amount for child tickets is ", child_total)
print("Total amount for child tickets is ", child_total)
print("popcorn quantity is ", popcorn_quantity)
print("Total amount for popcorn is ", popcorn_total)
print("Total Bill is ", total_amount)