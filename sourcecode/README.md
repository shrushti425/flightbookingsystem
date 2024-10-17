# ✈️ Airline Ticket Booking System 🛫 

---
## 🔧 Source Code Explaination

## 🧩 Part 1: Welcome and Login/Signup System

### 1️⃣ **Welcome Page**
   - Uses **simple print statements** to greet the user and explain the booking system.
      

### 2️⃣ **Login/Signup Page**
   - **Login**: Users are asked to enter their email id and password. 
     - The system checks if the entered credentials exist in a **list** for useremails and a **list** for passwords.
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
- The system checks if flights are available from a given city.
- The system converts inputs to **lowercase** for convenience.

### 2️⃣ Selecting Destination
- After choosing the departure city, the user selects a **destination** from the given options.
  - Cities like **Singapore** and **Dubai** are two options given.
  - Conditional statement and while loop used for the same.

### 3️⃣ Selecting Date & Time
- Users pick a **month**, and within that, choose a **date** and lastly the **flight time**.
    - Months are January and February, One can choose any date.
    - Then the available flight options are displayed.
    - Enter the serial number of the desired flight timing.

### 4️⃣ Price Calculation
- The sum is calculated as per the users choice.
- Number of tickets is taken and accordingly prices are calculated and discount is given.
- If number of tickets is greater than 5 then 10% discount and if the number of tickets is 10 then 20% discount
- Meal option is provided and 5000 is added accordingly.

### 3️⃣ Final Amount & Payment
- The final amount is displayed after all selections.

### 1️⃣ Printing Ticket 
- The system prints all the details about the flight and passenger in an organized manner using **for loops** and **lists**.
 

### 2️⃣ Presentation
- The ticket and boarding pass are designed for **clarity** and **professionalism**, simulating real airline tickets.

## 🚀 Technologies Used

- **Python**: Core programming language for logic implementation.
- **Lists, Dictionaries**: Essential data structures for user information, flight schedules, and pricing.
- **Conditional Statements**: To validate input and handle user login/signup.
- **loops**: While and for loop.
- **regular expressions module**:For checking if the password is strong or not.

## ✍️ Author

This project was developed by me- **Shrushti** as a solo effort to simulate a real-world airline booking system with detailed, modularized Python code.

Feel free to reach out for **collaboration** or **suggestions**!
