# ✈️ Airline Ticket Booking System 🛫 

---

## 🗓️ Timeline

This is a **solo project** split into four parts:

- **Part 1**: Welcome Page and Login/Signup System (Deadline: 12th Sept)
- **Part 2**: Choosing Location and Booking System (Deadline: 24th Sept)
- **Part 3**: Price Calculation and Payment (Deadline: 27st Sept)
- **Part 4**: Ticket Printing and Boarding Pass Generation (Deadline: 30th Sept)

---
## 🔧 Tech Perspectives

## 🧩 Part 1: Welcome and Login/Signup System

### 1️⃣ **Welcome Page**
   - Uses **simple print statements** to greet the user and explain the booking system.
      

### 2️⃣ **Login/Signup Page**
   - **Login**: Users are asked to enter their email id and password. 
     - The system checks if the entered credentials exist in a **list** for useremails and a **dictionary** for passwords.
     - If credentials match, the user is logged in. 
     - **Conditional statements** ensure only valid users can proceed.
   - **Signup**: 
     - New users provide a username and a password. The system suggests rules for creating a strong password:
       - Must contain: special character, number, uppercase letter.
       - **Password Strength Validation** is implemented using `if` conditions to check password validity.
     - If the password is weak, the user is informed about what's missing and asked to try again.

## 🌍 Part 2: Location and Ticket Booking System

### 1️⃣ Choosing Location
- The user is presented with a list of cities to travel **from** (e.g., Pune, Mumbai).
- Functions are created for each city for better **modularization**.
- The system converts inputs to **lowercase** for convenience.

### 2️⃣ Selecting Destination
- After choosing the departure city, the user selects a **destination** from a nested dictionary.
  - Cities like **Singapore**, **Hanoi**, and **Dubai** are the **keys** in the dictionary.
  - Nested within each destination are **dates** as keys, followed by available flight timings.

### 3️⃣ Selecting Date & Time
- Users pick a **date**, and within that, choose a **flight time**.
  - Each flight time contains a **tuple** that represents the available seats.
  - Seats are displayed as a **2D grid** and tracked as `True` for booked and `False` for available.

### 4️⃣ Price & Seat Selection
- The flight time dictionary also stores **prices** for different classes (Economy, Business, etc.).
- The user picks a class, and the price is added to the **SUM** variable.

## 💵 Part 3: Price Calculation and Payment

### 1️⃣ Add-Ons and Offers
- After selecting the flight, the user is prompted with a list of **add-ons** (e.g., meals, extra baggage).
- The price for each selected add-on is added to the **SUM** total.

### 2️⃣ Discounts & Coupons
- The system checks for applicable **offers** and subtracts the discount from the total amount if a valid **coupon** is provided.

### 3️⃣ Final Amount & Payment
- The final amount is displayed after all selections, and the user is asked for **payment confirmation**.

## 🎫 Part 4: Ticket Printing and Boarding Pass Generation

### 1️⃣ Printing Ticket and Boarding Pass
- The system prints all the details about the flight in an organized manner using **for loops** and **dictionaries**.
- A **boarding pass** is generated in a format similar to standard airlines, containing flight details, seat number, and payment information.

### 2️⃣ Presentation
- The ticket and boarding pass are designed for **clarity** and **professionalism**, simulating real airline tickets.

## 🚀 Technologies Used

- **Python**: Core programming language for logic implementation.
- **Lists, Dictionaries, and Tuples**: Essential data structures for user information, flight schedules, and pricing.
- **Conditional Statements**: To validate input and handle user login/signup.
- **Functions**: Modularized code for better organization and readability.

## ✍️ Author

This project was developed by **Shrushti** as a solo effort to simulate a real-world airline booking system with detailed, modularized Python code.

Feel free to reach out for **collaboration** or **suggestions**!
