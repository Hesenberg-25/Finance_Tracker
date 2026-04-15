from datetime import date
import csv
category = ["Food", "Transport", "Household", "Education", "Health", "Utilities", "Other"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def get_monthly_expense(monthr):
    total_expense=0
    found=False
    with open("Expenses.csv",'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(row['Month']==monthr):
                total_expense+=int(row['Amount'])
                found=True
    if(found==True):
        return total_expense
    else:
        return 0

def select_category(i):
    date_today=date.today()
    month_today=date_today.month
    print("\n")
    print(f"Category : {category[i-1]}")
    price=int(input("Enter the Amount Spend : "))
    print(f"Expense Spend on {category[i-1]} : {price}\n")
    with open("Expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_today,months[month_today-1].capitalize(),category[i-1].capitalize(),price])
    print("New Expense Added Successfully")
    print("\n")

def add_new_expense():
    print("Add New Expense :: ")
    print("\n")
    while(True):
        for i in range(7):
            print(f"{i+1}.{category[i]}")
        print("8.Exit")
        choice1=int(input("Enter Desired Category : "))
        if(choice1<=len(category)):
            select_category(choice1)
        else:
            break;

def see_desired_expense():
    print("See Desired Expense")
    desired_category=str(input("Enter the Desired Category : ").capitalize())
    desired_month=int(input("Enter the Month No (1 for Jan ...) : "))
    print(f"Detail Expenses on {desired_category} in month of {months[desired_month-1]} : ")
    total=0
    found_any=False
    with open("Expenses.csv",'r') as file :
        reader = csv.DictReader(file)
        print(f"\n{'Date':<15} | {'Amount':<10}")
        print("-"*28)
        for row in reader:
            if (row['Category']==desired_category and row['Month']==months[desired_month-1]):
                amount_see=float(row['Amount'])
                date_see=row['Date']
                total+=amount_see
                print(f"{row['Date']:<15} | {amount_see:<10}")
                found_any=True
    if not found_any:
        print("No Data Found")
    print("-"*28)
    print(f"Total Amount spend on {desired_category} : {total}")


#Summary Expense
def see_summary():
    print("See Summary")
    print("1. Monthly")
    print("2. Yearly")
    choice3 = int(input("Select the Timeline for Summary : "))

    #Yearly
    if choice3 == 2:
        total_yearly = 0
        found_any = False
        with open("Expenses.csv", 'r') as file:
            reader = csv.DictReader(file)
            print(f"\n{'Date':<15} | {'Amount':<10}")
            print("-" * 28)
            for row in reader:
                amount_see = float(row['Amount'])
                total_yearly += amount_see
                print(f"{row['Date']:<15} | {amount_see:<10}")
                found_any = True
        
        if not found_any:
            print("No Data Found")
        print("-" * 28)
        print(f"Total Amount spent Yearly: {total_yearly}")
        
    #Monthly
    elif choice3 == 1:
        desired_monthly = int(input("Enter the Month No (1 for Jan ...) : "))
        total_monthly = 0
        found_any = False
        
        with open("Expenses.csv", 'r') as file:
            reader = csv.DictReader(file)
            print(f"\n{'Date':<15} | {'Amount':<10}")
            print("-" * 28)
            for row in reader:
                if row['Month'] == months[desired_monthly-1]:
                    amount_see = float(row['Amount'])
                    total_monthly += amount_see
                    print(f"{row['Date']:<15} | {amount_see:<10}")
                    found_any = True
        
        if not found_any:
            print("No Data Found")
        print("-" * 28)
        print(f"Total Amount spent in {months[desired_monthly-1]} : ₹{total_monthly}")
    else:
        print("Invalid Input")

def menu_expense_tracker():
    print("Welcome to Expense Tracker")
    while (True):
        print("\n")
        print("1. Add New Expense")
        print("2. See Desired Category")
        print("3. See Summary")
        print("4. Exit")
        choice = (int(input("Enter Desired Option : ")))
        print("\n")
        if (choice == 1):
            add_new_expense()
        elif (choice == 2):
            see_desired_expense()
        elif (choice == 3):
            see_summary()
        elif (choice == 4):
            print("Thankyou for Visiting, Keep Earning !!!")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    menu_expense_tracker()
