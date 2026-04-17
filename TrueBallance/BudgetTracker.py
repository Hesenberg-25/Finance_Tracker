import ExpenseTracker 
import csv
import os

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def set_budget():
    print("--- Set Budget ---")
    month_set = int(input("Enter the Month No (1 for Jan ...) : "))
    budget = float(input("Enter Your Monthly Budget : "))
    month_name = months[month_set - 1]

    # Read existing data
    rows = []
    file_exists = os.path.isfile("Budget.csv")
    if file_exists:
        with open("Budget.csv", 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    # Check if month already exists
    updated = False
    for row in rows:
        if row['Month'] == month_name:
            row['Budget'] = budget
            updated = True
            break

    if not updated:
        rows.append({'Month': month_name, 'Budget': budget})
    with open("Budget.csv", 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Month", "Budget"])
        writer.writeheader()
        writer.writerows(rows)

    if updated:
        print(f"✅ Budget for {month_name} updated successfully!")
    else:
        print(f"✅ Budget for {month_name} saved successfully!")

def check_budget():
    print("--- Check Budget ---")
    month_check = int(input("Enter the Month No (1 for Jan ...) : "))
    month_name = months[month_check - 1]
    actual_expense = float(ExpenseTracker.get_monthly_expense(month_name))
    setted_budget = 0 
    file_exists = os.path.isfile("Budget.csv")
    with open("Budget.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Month'] == month_name:
                setted_budget = float(row['Budget'])
    print(f"Budget set by you in {month_name} : {setted_budget}")
    print(f"Expenses done by you in {month_name} till now : {actual_expense}")
    if actual_expense < setted_budget:
        remaining = setted_budget - actual_expense
        print(f"✅ Hushhh!! You still have {remaining} to spend. Use them wisely.")
    elif actual_expense > setted_budget:
        over = actual_expense - setted_budget
        print(f"⚠️ Warning!! You have exceeded your budget by {over}.")
    else:
        print("You are exactly on budget! Be careful.")

def menu_budget_tracker():
    print("Welocome To Budget Tracker")
    while (True):
        print("\n")
        print("1. Set Budget ")
        print("2. Check Budget v/s Actual")
        print("3. Exit")
        print("\n")
        choice=int(input("Enter Desired Input : "))
        if (choice==1):
            set_budget()
        elif (choice==2):
            check_budget()
        elif (choice==3):
            print("✅ Thankyou for Visiting, Keep Earning !!!")
            break
        else:
            print("⚠️ Invalid Input")

if __name__ == "__main__":
    menu_budget_tracker()
