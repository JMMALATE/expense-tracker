# Expense Tracker - Installment 3
# Author: John Michael Malate
# Adds tax, budget and a full summary.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)
print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
tax_percent = float(input("Tax percentage? "))
budget = float(input("Budget? "))
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total
print("-" * 40)
print("SUMMARY")
print(f"- {item1}:\t${amount1}")
print(f"- {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: John Michael Malate | Installment 3")