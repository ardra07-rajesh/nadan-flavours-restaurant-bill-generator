import random
from datetime import datetime

print("NADAN FLAVOURS")
print("Restaurant Bill Generator")

# Restaurant menu
menu = {
    "Breads": {
        "Chappathi": 12,
        "Porotta": 15,
        "Butter Naan": 30
    },

    "Breakfast": {
        "Idli": 30,
        "Dosa": 15,
        "Masala Dosa": 80,
        "Ghee Roast": 50,
        "Appam": 18,
        "Upma": 50
    },

    "Chicken Dishes": {
        "Chicken Curry": 140,
        "Chicken Fry": 120,
        "Chicken Roast": 170,
        "Butter Chicken": 200
    },

    "Vegetarian": {
        "Veg Kuruma": 120,
        "Paneer Butter Masala": 150,
        "Gobi Manchurian": 140
    },

    "Egg Dishes": {
        "Egg Roast": 50
    },

    "Seafood": {
        "Fish Fry": 200,
        "Fish Curry": 120,
        "Seafood Platter": 1500
    },

    "Meals": {
        "Kerala Meals": 80,
        "Kerala Sadhya": 200
    },

    "Biriyani": {
        "Chicken Biriyani": 170,
        "Fish Biriyani": 250,
        "Egg Biriyani": 120,
        "Veg Biriyani": 100
    }
}

# GST and Discount
GST_RATE = 0.05
DISCOUNT_LIMIT = 1000
DISCOUNT_RATE = 0.10

# Waiter Names
waiters = ["Rahul", "Anand", "Arjun", "Akhil", "Neha", "Anu"]

# Variables
ordered_items = {}
total_amount = 0

menu_items = []
item_number = 1

print("\n-------------------- MENU --------------------")

# Display Menu
for category in menu:
    print("\n" + category)

    for food in menu[category]:
        price = menu[category][food]
        print(item_number, ".", food, "- Rs.", price)

        menu_items.append((food, price))
        item_number += 1

print("\n0. Exit Ordering")

# Take Customer Order
while True:

    try:
        choice = int(input("\nEnter Item Number (0 to Finish): "))

        if choice == 0:
            break

        if choice < 1 or choice > len(menu_items):
            print("Invalid Item Number!")
            continue

        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Please enter a valid quantity.")
            continue

        food_name = menu_items[choice - 1][0]
        food_price = menu_items[choice - 1][1]

        if food_name in ordered_items:
            ordered_items[food_name][0] += quantity
            print(food_name, "updated successfully.")
        else:
            ordered_items[food_name] = [quantity, food_price]
            print(food_name, "added to your order.")

        more = input("\nDo you want to order another item? (y/n): ").lower()

        if more != "y" and more != "yes":
            break

    except ValueError:
        print("Please enter a valid number!")

# Customer Details
if ordered_items:

    prep_time = random.randint(10, 30)
    print("\nEstimated Time:", prep_time, "Minutes")

    waiter = random.choice(waiters)

    print("\n----------- CUSTOMER DETAILS -----------")

    customer_name = input("Enter Customer Name : ")
    customer_phone = input("Enter Phone Number : ")
    customer_table = input("Enter Table Number : ")

    print("\nSelect Dining Type")
    print("1. Dine In")
    print("2. Take Away")

    while True:
        dining_choice = input("Enter Choice (1/2): ")

        if dining_choice == "1":
            dining_type = "Dine In"
            delivery_charge = 0
            break

        elif dining_choice == "2":
            dining_type = "Take Away"
            delivery_charge = 40
            break

        else:
            print("Please choose 1 or 2.")

        print("\n----------- PAYMENT METHOD -----------")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    while True:
        payment_choice = input("Choose Payment Method (1-3): ")

        if payment_choice == "1":
            payment_method = "Cash"
            break

        elif payment_choice == "2":
            payment_method = "UPI"
            break

        elif payment_choice == "3":
            payment_method = "Card"
            break

        else:
            print("Please choose 1, 2 or 3.")

    payment_status = "PAID"

else:
    waiter = "N/A"
    customer_name = "N/A"
    customer_phone = "N/A"
    customer_table = "N/A"
    dining_type = "N/A"
    delivery_charge = 0
    payment_method = "N/A"
    payment_status = "N/A"
    
# Calculate Bill
for item in ordered_items:
    quantity = ordered_items[item][0]
    price = ordered_items[item][1]
    total_amount += quantity * price

discount = 0

if total_amount > DISCOUNT_LIMIT:
    discount = total_amount * DISCOUNT_RATE

taxable_amount = total_amount - discount
gst = taxable_amount * GST_RATE
grand_total = taxable_amount + gst + delivery_charge

total_items = 0

for item in ordered_items:
    total_items += ordered_items[item][0]

points = int(grand_total / 100)

bill_no = random.randint(1000, 9999)
order_no = random.randint(10000, 99999)
now = datetime.now()


# Bill Printing
print()
print("=" * 60)
print(f"{'NADAN FLAVOURS':^60}")
print(f"{'CUSTOMER BILL':^60}")
print("=" * 60)

print(f"Order No      : {order_no}")
print(f"Bill No       : {bill_no}")
print(f"Date          : {now.strftime('%d-%m-%Y')}")
print(f"Time          : {now.strftime('%I:%M %p')}")
print(f"Day           : {now.strftime('%A')}")
print(f"Customer Name : {customer_name}")
print(f"Phone Number  : {customer_phone}")
print(f"Table Number  : {customer_table}")
print(f"Served By     : {waiter}")
print(f"Dining Type   : {dining_type}")

if not ordered_items:
    print("\nNo items ordered.")

else:
    print("-" * 60)
    print(f"{'Item':<25}{'Qty':>5}{'Price':>12}{'Amount':>15}")
    print("-" * 60)

    for item in ordered_items:
        quantity = ordered_items[item][0]
        price = ordered_items[item][1]
        amount = quantity * price

        print(f"{item:<25}{quantity:>5}{price:>12.2f}{amount:>15.2f}")

    print("-" * 60)

    print(f"Total Items      : {total_items}")
    print(f"Subtotal         : Rs. {total_amount:.2f}")

    if discount > 0:
        print(f"Discount         : Rs. {discount:.2f}")

    print(f"GST (5%)         : Rs. {gst:.2f}")

    if delivery_charge > 0:
        print(f"Delivery Charge  : Rs. {delivery_charge:.2f}")

    print("=" * 60)
    print(f"Grand Total      : Rs. {grand_total:.2f}")
    print("=" * 60)

    print(f"Payment Method   : {payment_method}")
    print(f"Payment Status   : {payment_status}")
    print(f"Reward Points    : {points}")

    if grand_total >= 2000:
        print("\nCongratulations! Free Dessert Included!")

print("=" * 60)
print("Thank You for Dining with Us!".center(60))
print("Visit Again - Nadan Flavours".center(60))
print("Taste of Kerala".center(60))
print("=" * 60)