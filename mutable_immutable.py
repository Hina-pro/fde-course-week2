"""import copy

original = [[100, 200], [300, 400]]

copied = copy.deepcopy(original)

copied[0][0] = 999

print(original)
print(copied)"""

# Example # 2

"""original = [100, 200, 300]
copied = original.copy()

copied[0] = 999

print(original)
print(copied)"""

# Mutable and immutable problems # 1

"""code = "ord-0042"

code = code.upper()

code = code.replace("-", "")

print(code)"""


# Problem # 2


"""names = [" amna ", "BILAL", " zara khan"]

cleaned_names = []

for name in names:
    clean = name.strip().title()
    cleaned_names.append(clean)

print(cleaned_names)"""

# Problem # 3

"""sku = "PEN-O42"
sku = sku.replace("O", "0")

print(sku)"""


# list example

"""prices = [850, 1200, 400]

prices.append(3100)

prices[0] = 900

print(prices)"""

# Problems of List
# Problem # 1

"""cart = ["rice", "oil"]

cart.append("sugar")

cart[1] = "ghee"

cart.remove("rice")

print(cart)"""

# Problem # 2

"""stock = {"pens": 120, "notebooks": 45}
stock["pens"] = stock["pens"] - 20
stock["markers"] = 60
del stock["notebooks"]
print(stock)"""

# proble # 3

"""prices = [850, 1200, 400]

for i in range(len(prices)):
    prices[i] = round(prices[i] * 1.1)

print(prices)"""


# Problems of Id

# Example
"""status = "pending"
before = id(status)
status = status.upper()
print(id(status) == before)

order = {"status": "pending"}
before = id(order)
order["status"] = "delivered"
print(id(order) == before)"""

# Problem # 1


"""status = "pending"
before = id(status)
status = status.upper()
print(id(status) == before)
order = {"status": "pending"}
before = id(order)
order["status"] = "delivered"
print(id(order) == before)"""

# problem # 2


"""a = [4500, 12800]
b = a
c = a.copy()
print(id(a) == id(b), id(a) == id(c))"""

# Example 2


"""a = [4500, 12800]
b = a
c = a.copy()
print(a is b, a is c)"""

# problem # 3


"""prices = [1200, 400, 850]

before = id(prices)

prices.sort()
print(prices)
print(id(prices) == before)

prices = sorted(prices, reverse=True)
print(prices)
print(id(prices) == before)"""

# Tuple
# Problem # 1

"""line = ("Rice", 2, 1450)

print(f"{line[1]} x {line[0]} = Rs {line[1] * line[2]:,}")"""

# Problem # 2


"""lines = [("Rice", 2, 1450), ("Oil", 1, 2100), ("Sugar", 3, 160)]

total = 0

for line in lines:
    item, quantity, price = line
    order_total = quantity * price
    total = total + order_total

print(total)"""

# Problem # 3


"""cart = ["Rice", "Oil", "Sugar"]  # List: Items can be added or removed.

date = (2026, 11, 3)  # Tuple: Stores a fixed group of date values.

orders = ["Order 1", "Order 2", "Order 3"]  # List: New orders can arrive.

location = (33.6844, 73.0479)  # Tuple: Latitude and longitude form a fixed pair.

print(cart)
print(date)
print(orders)
print(location)"""

# example

"""todays_orders = [4500, 12800]
report_orders = todays_orders.copy()
report_orders.append(2300)
print(todays_orders)
print(report_orders)"""


# Two names one list
# examples

"""vip = ["Noor Foods"]
all_customers = vip
all_customers.append("Bilal Traders")
print(vip)
print(all_customers)"""

# example 2

"""vip = ["Noor Foods"]
all_customers = vip

all_customers.append("Bilal Traders")
all_customers.append("ABC School")

print(vip)"""
# example

"""a = [100, 200]
b = a
b.append(300)
a.append(400)
print(b)"""


# Problem # 1

"""vip = ["Noor Foods"]
all_customers = vip.copy()
all_customers.append("Bilal Traders")
print("VIP Customers:", vip)
print("All Customers:", all_customers)"""

# Example

"""vip = ["Noor Foods"]
all_customers = vip.copy()
all_customers.append("ABC School")
print(vip)"""

# Example

"""a = [10, 20]
b = a.copy()

b.append(30)

print(a)
print(b)"""

# Problem # 2

"""lines = [("Rice", 2, 1450), ("Oil", 1, 2100), ("Sugar", 3, 160)]

grand_total = 0

for item, quantity, price in lines:
    total = quantity * price
    grand_total = grand_total + total

    print(item, "Total: Rs", total)

print("Grand Total: Rs", grand_total)"""

# problem # 3


"""city = "Karachi"
branch = city
branch = branch + " Branch"
print(city)
orders = [4500]
report = orders
report = report + [2300]
print(orders)"""


# function
# Problem # 1


"""def close_order(order):
    order["status"] = "closed"


def closed_copy(order):
    new_order = order.copy()
    new_order["status"] = "closed"
    return new_order


order = {"id": "A101", "status": "pending"}

close_order(order)
print("After close_order:", order["status"])
order = {"id": "A101", "status": "pending"}
new_order = closed_copy(order)
print("Original order:", order)
print("Copied order:", new_order)"""

# Problem # 2


"""def rename(customer):
    customer = "Bilal Traders"


def empty_cart(cart):
    cart = []


name = "Noor Foods"
rename(name)
print(name)

cart = ["rice", "oil"]
empty_cart(cart)
print(cart)"""

# problem # 3

# This function changes the original cart.
# Its name tells us that it adds an item directly.


def add_item(cart, item):
    cart.append(item)


# This function returns a new cart.
# Its name tells us to expect a cart with the new item,
# without changing the original cart.


def with_item(cart, item):
    new_cart = cart.copy()
    new_cart.append(item)
    return new_cart


# Starting cart

"""cart = ["Rice", "Oil"]

print("Starting cart:", cart)
add_item(cart, "Sugar")
rint("After add_item:", cart)
new_cart = with_item(cart, "Milk")

print("After with_item - Original cart:", cart)
print("New cart:", new_cart)"""
