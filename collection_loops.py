# Example of loop

"""students = ["Ali", "Sara", "Ahmed", "Hina", "Bilal"]

for student in students:
    print(student)"""

# example of set

"""priorities = {"low", "medium", "urgent"}

print(len(priorities))
print("urgent" in priorities)
print("critical" in priorities)
print(sorted(priorities))"""

# Problem 1 set

"""cities = ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"]

unique_cities = set(cities)

print(len(unique_cities))

print(sorted(unique_cities))"""

# problem # 2

"""order_ids = ["A101", "A102", "A101", "A103", "A102"]

seen = set()

for order in order_ids:
    if order in seen:
        print("Duplicate:", order)
    else:
        seen.add(order)"""

# Example

"""this_week = {"Noor Foods", "Bilal Traders", "Karachi Crafts"}
last_week = {"Noor Foods", "Zara Textiles"}

# print(sorted(this_week & last_week))
# print(sorted(this_week - last_week))
print(sorted(this_week | last_week))"""


# Example

"""raw_orders = [
    {"customer": " noor foods ", "status": "Delivered", "paid": 1},
    {"customer": "BILAL TRADERS", "status": " pending ", "paid": 0},
    {"customer": "noor foods", "status": "PENDING", "paid": 0},
]

orders = []
for raw in raw_orders:
    orders.append(
        {
            "customer": raw["customer"].strip().title(),
            "status": raw["status"].strip().lower(),
            "paid": bool(raw["paid"]),
        }
    )

for order in orders:
    print(order)

customers = set()
for order in orders:
    customers.add(order["customer"])
print(sorted(customers))"""


"""raw_tickets = [
    {"title": " refund not received ", "priority": "High", "open": 1},
    {"title": "late delivery", "priority": " urgent ", "open": 0},
    {"title": "WRONG ITEM SENT", "priority": "MEDIUM", "open": 1},
    {"title": "Late delivery ", "priority": "low", "open": 1},
]


def clean_tickets(raw_tickets):
    tickets = []

    for raw in raw_tickets:
        cleaned = {
            "title": raw["title"].strip().capitalize(),
            "priority": raw["priority"].strip().lower(),
            "open": bool(raw["open"]),
        }

        tickets.append(cleaned)

    return tickets


cleaned_tickets = clean_tickets(raw_tickets)

open_tickets = 0

for ticket in cleaned_tickets:
    if ticket["open"]:
        open_tickets += 1

titles = set()
priorities = set()

for ticket in cleaned_tickets:
    titles.add(ticket["title"])
    priorities.add(ticket["priority"])

print("Open tickets:", open_tickets)
print("Different titles:", len(titles))
print("Priorities:", sorted(priorities))

print("Original data:", raw_tickets)"""

# problem # 3

"""last_month = {"Noor Foods", "Bilal Traders", "Zara Textiles"}

this_month = {"Noor Foods", "Karachi Crafts"}

lost = last_month - this_month
new = this_month - last_month
stayed = last_month & this_month

print("Lost:", sorted(lost))
print("New:", sorted(new))
print("Stayed:", sorted(stayed))"""


# spilting and joining
# Examples

"""name = "Hina Sultan"
result = name.split()
print(result)"""

# Example # 2


"""names = ["Hina", "Sultan"]

result = " ".join(names)

print(result)"""

# Example

"""text = "Karachi Lahore Islamabad"

cities = text.split()

result = ", ".join(cities)

print(result)"""

# Problem # 1

"""line = "A102,Karachi Crafts,12800,pending"

parts = line.split(",")
order_id = parts[0]
customer = parts[1]
amount = parts[2]
status = parts[3]
amount = int(amount)

print(f"{customer} owes Rs {amount:,}")"""

# Problem # 2

"""tags = "rice, oil ,sugar "

# Step 1: Split at commas
parts = tags.split(",")

# Step 2: Create an empty list
cleaned = []

# Step 3: Remove extra spaces
for part in parts:
    cleaned.append(part.strip())

# Step 4: Join with |
result = " | ".join(cleaned)

# Step 5: Print result
print(result)"""

# Problem # 3

'''totals = [4500, 12800, 2300]

# Step 1: Create an empty list
string_totals = []

# Step 2: Convert numbers into strings
for amount in totals:
    string_totals.append(str(amount))

# Step 3: Join strings with + sign
result = " + ".join(string_totals)

# Step 4: Calculate the total
total = sum(totals)

# Step 5: Print final result
print(f"{result} = {total}")"""

# Sorting's example

names = []
names.append("Hina")
names.append("Sultan")

print(names)

# Strip problem # 1

names = ["Noor", "Bilal", "Amna"]

# Create a new sorted list
result = sorted(names)
print(result)
print(names)'''

# Class and objects
# Examples


"""class Student:
    name = "Hina"
    age = 35


student1 = Student()

print(student1.name)
print(student1.age)"""

# Example 2


"""class Car:
    brand = "Toyota"
    color = "Black"


car1 = Car()

print(car1.brand)
print(car1.color)"""

# Example 3


"""class Employee:
    name = "Ali"
    salary = 50000
    department = "Accounts"


employee1 = Employee()

print(employee1.name)
print(employee1.salary)
print(employee1.department)"""

# Examples


"""class Student:
    name = "Hina"


class Car:
    brand = "Toyota"


# Objects
student1 = Student()
car1 = Car()

print(student1.name)
print(car1.brand)"""


# Examples


"""class Customer:
    def __init__(self, name):
        self.name = name


noor = Customer("Noor Foods")
bilal = Customer("Bilal Traders")

print(noor.name)
print(bilal.name)"""

# example


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name)
        print(self.salary)


emp1 = Employee("Ali", 50000)
emp2 = Employee("Sara", 60000)

emp1.show_details()
emp2.show_details()
