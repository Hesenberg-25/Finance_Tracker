# Personal Finance Suite — Python

A beginner fintech project suite built in Python, integrating three financial tools into one unified system.

> "Users don't just want to see a list of what they spent — they want the app to tell them how to be better with money."

---

## Project Structure

```
Personal-Finance-Suite/
│
├── Integration.py          # Main file from where others are operated
├── ExpenseTracker.py       # Track daily expenses by category
├── InterestCalculator.py   # SI, CI, EMI, SIP, Tax calculations
├── BudgetTracker.py        # Set budgets and compare vs actual spending
│
├── Expenses.csv            # Auto-generated — stores expense records
├── Budget.csv              # Auto-generated — stores monthly budgets
│
└── README.md
```

---

## The Three Modules

---

### 1. Expense Tracker (`ExpenseTracker.py`)

A daily expense logging system that stores all spending in a local CSV file and lets you view it sliced by category, month, or year.

**Features:**

#### Add New Expense
- Choose from 7 predefined categories: **Food, Transport, Household, Education, Health, Utilities, Other**
- Automatically captures today's date using `datetime` — no manual date entry
- Detects the current month automatically and tags the entry
- Appends the record to `Expenses.csv` in the format: `Date | Month | Category | Amount`
- Supports adding multiple expenses in one session without restarting

#### View Desired Category Expense
- Filter expenses by any specific **category + month** combination
- Displays a clean formatted table showing each entry's date and amount
- Shows the **total spend** for that category in that month at the bottom
- Handles missing data gracefully — prints "No Data Found" instead of crashing

#### Summary View
- **Monthly Summary** — Enter any month number (1–12) and get a full line-by-line breakdown of every expense that month, with a total at the end
- **Yearly Summary** — Dumps every single expense record across all months in one view with a grand total
- Both summaries use a formatted table (`Date | Amount`) for readability

---

### 2. Interest Calculator (`InterestCalculator.py`)

A financial calculator covering five real-world personal finance scenarios — from basic interest to tax filing and investment planning.

**Features:**

#### Simple Interest
- Inputs: Principal amount, interest rate (%), time period (in years)
- Formula: `SI = (P × R × T) / 100`
- Outputs: Interest earned and total maturity amount
- Useful for: Fixed deposits, basic loan estimates

#### Compound Interest
- Inputs: Principal, annual interest rate, time period, compounding frequency
- Supports all 4 real-world compounding frequencies:
  - **Yearly** (n=1), **Half-Yearly** (n=2), **Quarterly** (n=4), **Monthly** (n=12)
- Formula: `A = P × (1 + r/n)^(n×t)`
- Outputs: Interest earned and total maturity amount
- Useful for: Bank FDs, recurring deposits, savings accounts

#### Loan Amortization Schedule
- Inputs: Loan amount, annual interest rate, loan tenure (in months)
- Calculates your **EMI** using the standard formula:
  `EMI = P × r × (1+r)^n / ((1+r)^n - 1)`
- Generates a **full month-by-month repayment table** showing:
  - Opening balance
  - Interest component for that month
  - Principal component for that month
  - Closing balance after payment
- Automatically zeroes out the balance in the final month (handles floating point drift)
- Useful for: Home loans, car loans, personal loans — understanding exactly how much of your EMI is interest vs principal

#### Income Tax Calculator (Indian New Tax Regime — FY 2024-25)
- Input: Gross annual salary (including bonuses)
- Automatically applies **₹75,000 standard deduction** before calculating taxable income
- Calculates tax using the latest New Regime slabs
- Outputs: Taxable income, total tax payable, net in-hand salary
- If salary is below the tax-free threshold, displays a "✅ No Tax Imposed" message
- Useful for: Salary planning, understanding your actual take-home pay

#### SIP Calculator (Systematic Investment Plan)
- Inputs: Monthly investment amount, expected annual return rate (%), investment duration (in years)
- Uses the standard SIP future value formula with monthly compounding:
  `M = P × ((1 + r)^n - 1) / r × (1 + r)`
- Outputs:
  - Total amount invested (principal only)
  - Total maturity amount
  - Profit/wealth gained through compounding
- Useful for: Mutual fund planning, long-term wealth building, understanding the power of compounding over time

---

### 3. Budget Tracker (`BudgetTracker.py`)

Sets monthly spending limits and compares them against real expense data pulled directly from the Expense Tracker — the integration layer of the suite.

**Features:**

#### Set Monthly Budget
- Input: Month number and a budget amount in ₹
- Saves the budget to `Budget.csv`
- **Upsert logic** — if a budget for that month already exists, it gets **updated in place** instead of creating a duplicate row
- Gives different confirmation messages for new entries vs updates: "saved" vs "updated"
- Safe on first run — creates `Budget.csv` with headers automatically if it doesn't exist yet

####  Check Budget vs Actual
- Input: Month number
- Pulls **live actual spending** for that month directly from `ExpenseTracker.get_monthly_expense()` — no manual re-entry
- Reads the budget you set for that month from `Budget.csv`
- Compares the two and gives a status message:
  - **Under budget** → Shows exact remaining balance with a positive message
  - **Over budget** → Shows exact overspend amount with a warning
  - **Exactly on budget** → Caution message to stay careful
- Guards against the case where `Budget.csv` doesn't exist yet (first-time users who check before setting a budget)

---

## How the Integration Works

```
ExpenseTracker.py  ==>  Expenses.csv
                              ↑
BudgetTracker.py   ==>  Budget.csv
        └── imports get_monthly_expense() from ExpenseTracker.py

```
```
ExpenseTracker.py ──────|
BudgetTracker.py ───────|──────> Integaration.py
InterestCalculator.py ──|
```

`BudgetTracker` directly imports `ExpenseTracker` to pull live monthly totals — no manual data entry duplication.

---

The CSV files are created automatically on first run — No setup needed.

---

## CSV File Format

**Expenses.csv**
| Date       | Month | Category  | Amount |
|------------|-------|-----------|--------|
| 2025-04-10 | Apr   | Food      | 250    |

**Budget.csv**
| Month | Budget  |
|-------|---------|
| Apr   | 8000.0  |

---
