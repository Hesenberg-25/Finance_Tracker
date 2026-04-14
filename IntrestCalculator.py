import math

def simple_intrest():
    print("--- Simple Intrest ---")
    print("\n")
    try :
        principal=float(input("Enter Pricipal Amount : "))
        rate=float(input("Enter Intrest Rate (in %) : "))
        years=float(input("Enter Time (in Years) : "))
        intrest=(principal*rate*years)/100
        total_return=principal+intrest
        print("\n")
        print("-"*30)
        print(f"Intrest Earned : ₹{intrest:.2f}" )
        print(f"Total Matuarity Amount : ₹{total_return:.2f}")
        print("-"*30)
        print("\n")
    except:
        print(" ⚠️ Invalid Input")
 
def compound_intrest():
    print("--- Compound Intrest ---")
    print("\n")
    try :
        principal=float(input("Enter Pricipal Amount : "))
        rate=float(input("Enter Intrest Rate (in %) : "))/100
        years=float(input("Enter Time (in Years) : "))
        print("1. Yearly\n2. Half-Yearly\n3. Quaterly\n4. Monthly")
        frequency=int(input("Enter the Compound Frequency (in 1,2,4,12): "))
        total_return = principal * pow((1 + (rate / frequency)), (frequency * years))
        intrest=total_return-principal
        print("\n")
        print("-"*30)
        print(f"Intrest Earned : ₹{intrest:.2f}" )
        print(f"Total Matuarity Amount : ₹{total_return:.2f}")
        print("-"*30)
        print("\n")
    except:
        print(" ⚠️ Invalid Input")

def loan_amortization():
    print("--- Loan Amortization Schedule ---")
    print("\n")
    try:
        # Input
        principal=float(input("Enter your Loan Amount : "))
        annual_rate=float(input("Enter your Annual Intrest : "))
        time=float(input("Enter Loan Tenure (in Months ): "))

        # Calculation
        rate=annual_rate/(12*100)
        common_factor=pow((1+rate),time)
        emi=principal*rate*((common_factor)/(common_factor-1))

        # Results
        print(f"Your Monthly EMI is : {emi:.2f}\n")
        balance=principal
        print("-" * 75)
        print(f"{'Month':<8} | {'Opening Bal':<15} | {'Interest':<12} | {'Principal':<12} | {'Closing Bal':<15}")
        print("-" * 75)
        for i in range(1,int(time)+1):

            # Calculation for Ratio Proportion

            monthly_intrest=balance*rate
            monthly_principal=emi-monthly_intrest
            opening_balance=balance
            balance=opening_balance-monthly_principal
            if balance < 0: balance = 0

            # Results
            print(f"{i:<8} | {opening_balance:>15.2f} | {monthly_intrest:>12.2f} | {monthly_principal:>12.2f} | {balance:>15.2f}")
        print("-" * 75)
    except:
        print(" ⚠️ Invalid Input")
        

def taxation():
    print("---  Income Tax Calculator ---")
    print("\n")
    try:
        # Input
        salary = float(input("Enter your Annual Salary (Gross including bonuses): ₹"))
        
        # Standard Deduction (₹ 75000)
        taxable_income = salary - 75000
        if taxable_income < 0:
            taxable_income = 0
        tax = 0.0
 
        # Slabs: 0-3L (0%), 3-6L (5%), 6-9L (10%), 9-12L (15%), 12-15L (20%), Above 15L (30%)
        if taxable_income > 1500000:
            tax = (taxable_income - 1500000) * 0.30 + 150000
        elif taxable_income > 1200000:
            tax = (taxable_income - 1200000) * 0.20 + 90000
        elif taxable_income > 900000:
            tax = (taxable_income - 900000) * 0.15 + 45000
        elif taxable_income > 600000:
            tax = (taxable_income - 600000) * 0.10 + 15000
        elif taxable_income > 300000:
            tax = (taxable_income - 300000) * 0.05
        else:
            tax = 0
        in_hand=salary-tax

        # Results Display
        print("\n" + "-"*45)
        if tax > 0:
            print(f"Gross Annual Salary : ₹{salary:.2f}")
            print(f"Standard Deduction  : ₹75,000.00")
            print(f"Taxable Income      : ₹{taxable_income:.2f}")
            print("-" * 45)
            print(f"Total Tax Patable   : ₹{tax:.2f}")
            print(f"Net In-Hand         : ₹{in_hand:.2f}")
        else:
            print(f"Salary: ₹{salary:,.2f} | Status: ✅ No Tax Imposed")
        print("-"*45 + "\n")

    except :
        print(" ⚠️ Invalid Input")


def sip():
    print("--- SIP ---")
    print("\n")
    try:
        # Inputs : 
        principal_monthly=float(input("Enter your monthly Investment : "))
        annual_intrest_rate=float(input("Enter your Intrest Rate : "))
        duration=float(input("Enter the duration (in Years) : "))
        compound_frequency=annual_intrest_rate/(100*12)
        time_frequency=duration*12

        # Hidden Calculations : 
        growth_factor=((pow((1+compound_frequency),time_frequency)-1)/compound_frequency)
        matuarity_amount=(principal_monthly)*(growth_factor)*(1+compound_frequency)
        invested_amount=principal_monthly*time_frequency
        profit_gained=matuarity_amount-invested_amount

        # Results : 
        print("\n")
        print("-"*70)
        print(f"Your total Investment : ₹{invested_amount:.2f}")
        print(f"Total Matured Amount : ₹{matuarity_amount:.2f}")
        print(f"Profit gained through this Investment : ₹{profit_gained:.2f}")
        print("-"*70)
        print("\n")
    except:
        print(" ⚠️ Invalid Input")


if __name__ == "__main__":
    print("Welcome to Intrest Calculator")
    while True:
        print("\n")
        print("1. Simple Intrest")
        print("2. Compound Intrest")
        print("3. Loan Amortization Schedule")
        print("4. Taxation")
        print("5. SIP")
        print("6. Exit")
        print("\n")
        choice=int(input("Enter Desired Input : "))
        if choice==1:
            simple_intrest()
        elif choice==2:
            compound_intrest()
        elif choice==3:
            loan_amortization()
        elif choice==4:
            taxation()
        elif choice==5:
            sip()
        elif choice==6:
            print("✅ Thankyou for Visiting, Keep Earning !!!\n")
            break
        else:
            print(" ⚠️ Invalid Input")