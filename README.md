# 🍽️ Nadan Flavours – Restaurant Bill Generator

A Python-based console application that simulates a restaurant billing system. The application allows customers to select food items, enter quantities, calculate the bill, apply discounts and GST, select a dining type and payment method, and generate a formatted customer bill.

## 📌 Project Description

**Nadan Flavours – Restaurant Bill Generator** is a console-based Python application developed to automate the basic billing process of a restaurant.

The program provides a categorized restaurant menu where users can select food items and enter quantities. It automatically calculates the subtotal, applies a discount for eligible orders, calculates GST, adds the applicable Take Away charge, and generates the final bill.

The application also collects customer details and includes additional features such as random waiter assignment, estimated preparation time, order number, bill number, reward points, and a free dessert offer for bills of ₹2,000 or more.

## ✨ Features

* Categorized restaurant menu
* Food item selection using item numbers
* Quantity-based ordering
* Automatic subtotal calculation
* 10% discount for orders above ₹1,000
* 5% GST calculation
* Dine In and Take Away options
* ₹40 Take Away charge
* Cash, UPI, and Card payment options
* Customer information collection
* Random waiter assignment
* Random order number generation
* Random bill number generation
* Estimated food preparation time
* Reward points calculation
* Free dessert offer for bills of ₹2,000 or more
* Input validation
* Exception handling
* Formatted customer bill

## 🛠️ Technologies Used

* **Python**
* `random` module
* `datetime` module

## 🧠 Concepts Used

This project demonstrates the following Python concepts:

* Variables and data types
* Lists
* Dictionaries
* Nested dictionaries
* Loops
* Conditional statements
* `try-except` exception handling
* User input
* Arithmetic operations
* String formatting
* Importing Python modules
* Data validation

## 🧾 Billing Process

The program follows this calculation flow:

```text
Food Price × Quantity
        ↓
     Subtotal
        ↓
 Discount if applicable
        ↓
   Taxable Amount
        ↓
      5% GST
        ↓
 Take Away Charge
        ↓
    Grand Total
```

### Discount Rule

Orders above ₹1,000 receive a **10% discount**.

### GST Rule

A **5% GST** is calculated after applying the discount.

### Take Away Rule

A **₹40 Take Away charge** is added when the customer selects Take Away.

### Reward Points

Customers receive **1 reward point for every ₹100** spent based on the final bill amount.

### Free Dessert

Customers with a final bill of **₹2,000 or more** receive a free dessert.

## ▶️ How to Run

### Step 1 – Install Python

Make sure Python is installed on your computer.

You can check it using:

```bash
python --version
```

### Step 2 – Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/nadan-flavours-restaurant-bill-generator.git
```

### Step 3 – Open the Project

```bash
cd nadan-flavours-restaurant-bill-generator
```

### Step 4 – Run the Program

```bash
python restaurant_bill_generator.py
```

## 💻 Sample Workflow

The application follows these steps:

1. Display the restaurant menu
2. Select food items
3. Enter quantity
4. Add more items if required
5. Enter customer details
6. Select Dine In or Take Away
7. Select payment method
8. Calculate subtotal
9. Apply discount if eligible
10. Calculate GST
11. Add Take Away charge if applicable
12. Generate the final bill
13. Display reward points and special offers

## 🎯 Learning Outcomes

This project helped me understand how Python programming concepts can be combined to solve a real-world problem.

Through this project, I gained practical experience in handling user input, storing data using dictionaries and lists, performing calculations, using loops and conditional statements, validating input, handling errors, importing standard Python modules, and formatting output.

## 🚀 Future Improvements

The project can be further improved by adding:

* Graphical User Interface (GUI)
* Database connectivity
* Bill history
* Customer order history
* Digital receipt generation
* Admin login
* Menu management
* Online payment integration
* Inventory management
* PDF bill generation

## 📂 Project Structure

```text
nadan-flavours-restaurant-bill-generator/
│
├── restaurant_bill_generator.py
└── README.md
```

## 👨‍💻 Author

**Ardra Rajesh**

B.Tech Computer Science and Engineering
Generative AI Specialization

---

⭐ If you found this project interesting, feel free to explore the repository!
