import ExpenseTracker
import BudgetTracker
import IntrestCalculator

while (True):
    print("\n")
    print("1. Expense Tracker")
    print("2. Budget Tracker")
    print("3. Intrest Calculator")
    print("4. Exit")
    main_choice = (int(input("Enter Desired Option : ")))
    print("\n")
    if (main_choice == 1):
        ExpenseTracker.menu_expense_tracker()
    elif (main_choice == 2):
        BudgetTracker.menu_budget_tracker()
    elif (main_choice == 3):
        IntrestCalculator.menu_intrest_calculator()
    elif (main_choice == 4):
        print("Thankyou for Visiting, Keep Earning !!!")
        break
    else:
        print("Invalid Input")