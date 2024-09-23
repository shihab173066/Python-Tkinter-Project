"""
**Question**

Determining the price of a movie ticket

**Task Description:**

You need to create a program that will determine the price of a movie ticket. The program will calculate the ticket 
price based on the user's age and the time of the show, following specific rules. 
Additionally, there will be a special discount for shows before 5:00 PM.

**Task:**

Your task is to write a Python program that takes the user's age and showtime as 
input and calculates the ticket price. The program should operate according to the following rules:

**Conditions for determining the ticket price:**

1.  Ticket price based on age:
   - Age 10 and below: 300 BDT
   - Age 11-25: 500 BDT
   - Age 26-60: 800 BDT
   - Age above 60: 400 BDT

2.  Discount based on showtime:
   - If the showtime is before 5:00 PM (1700), a 10% discount on the ticket price will apply.

3.  Ensure valid input:
   - The age must be a positive integer.
   - The showtime must be in 24-hour format (HHMM) with a valid input.

**Input Format:**
1.  Age: A positive integer, such as 25, 40, etc.
2.  Showtime: Time in 24-hour format (HHMM), where the first two digits represent hours and the last two digits represent minutes. No spaces or characters between hours and minutes. For example, 7:10 AM -> 0710, 3:30 PM -> 1530, 6:45 PM -> 1845, etc.

**Output Format:**
The program will print the ticket price. If a discount applies, the output will display the discounted price as well.

**Sample Inputs and Outputs:**

Sample 1:  
Input:  
Age: 8  
Showtime (HHMM): 1630  
Output:  
Ticket price: 300 BDT  
Discount: 30.00 BDT  
Discounted price: 270.00 BDT

Sample 2:  
Input:  
Age: 22  
Showtime (HHMM): 1800  
Output:  
Ticket price: 500 BDT  
Discount: 0.00 BDT  
Discounted price: 500.00 BDT

Sample 3:  
Input:  
Age: 65  
Showtime (HHMM): 1545  
Output:  
Ticket price: 400 BDT  
Discount: 40.00 BDT  
Discounted price: 360.00 BDT

Sample 4:  
Input:  
Age: -5  
Showtime (HHMM): 1730  
Output:  
Invalid input. Age must be a positive integer.

Sample 5:  
Input:  
Age: 25  
Showtime (HHMM): 2500  
Output:  
Invalid input. Please provide the showtime in the correct format.

"""

import tkinter as tk
from tkinter import messagebox

def Ticket_Price_Calculation():
    try:
        AGE = int(age_entry.get())
        SHOWTIME = showtime_entry.get()

        if AGE <= 0:
            raise ValueError("Invalid input. Age must be a positive integer.")
        
        if not (SHOWTIME.isdigit() and len(SHOWTIME) == 4 and 0 <= int(SHOWTIME[:2]) < 24 and 0 <= int(SHOWTIME[2:]) < 60):
            raise ValueError("Invalid input. Please provide the showtime in the correct format.")
        
        if AGE <= 10:
            price = 300
        elif 11 <= AGE <= 25:
            price = 500
        elif 26 <= AGE <= 60:
            price = 800
        else:
            price = 400

        discount = 0.0
        if int(SHOWTIME) < 1700:
            discount = 0.10 * price
        
        discounted_price = price - discount

        ticket_price_label.config(text=f"Ticket Price: {price} BDT")
        discount_label.config(text=f"Discount Price: {discount:.2f} BDT")
        discounted_price_label.config(text=f"Discounted Price: {discounted_price:.2f} BDT")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def clear_entries():
    age_entry.delete(0, tk.END)
    showtime_entry.delete(0, tk.END)
    ticket_price_label.config(text="")
    discount_label.config(text="")
    discounted_price_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Movie Ticket Price Calculator")
root.geometry("400x300")

# Age input
age_label = tk.Label(root, text="Age:")
age_label.pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

# Showtime input
showtime_label = tk.Label(root, text="Showtime (HHMM):")
showtime_label.pack(pady=5)
showtime_entry = tk.Entry(root)
showtime_entry.pack(pady=5)

# Calculate Button
calculate_btn = tk.Button(root, text="Calculate Price", command=Ticket_Price_Calculation)
calculate_btn.pack(pady=10)

# Labels for displaying output
ticket_price_label = tk.Label(root, text="")
ticket_price_label.pack(pady=5)

discount_label = tk.Label(root, text="")
discount_label.pack(pady=5)

discounted_price_label = tk.Label(root, text="")
discounted_price_label.pack(pady=5)

# Clear Button
clear_btn = tk.Button(root, text="Clear", command=clear_entries)
clear_btn.pack(pady=5)

# Run the GUI loop
root.mainloop()
