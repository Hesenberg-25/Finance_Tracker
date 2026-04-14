# 💰 Personal Finance Suite — Python

A beginner fintech project suite built in Python, integrating three financial tools into one unified system.

> "Users don't just want to see a list of what they spent — they want the app to tell them how to be better with money."

---

## 📁 Project Structure

```
Personal-Finance-Suite/
│
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

## 🧩 The Three Modules

### 1. 🧾 Expense Tracker (`ExpenseTracker.py`)

Track and categorize your daily expenses. All data is stored in `Expenses.csv`.

**Features:**
- Add expenses across 7 categories: Food, Transport, Household, Education, Health, Utilities, Other
- View expenses filtered by category and month
- Monthly and yearly summary

**Run it:**
```bash
python ExpenseTracker.py
```

---

### 2. 📊 Interest Calculator (`InterestCalculator.py`)

A financial calculator covering five real-world use cases.

**Features:**
- **Simple Interest** — Principal, rate, time
- **Compound Interest** — Supports yearly, half-yearly, quarterly, monthly compounding
- **Loan Amortization Schedule** — Full month-by-month EMI breakdown
- **Income Tax Calculator** — Based on Indian New Tax Regime slabs (FY 2024-25), with ₹75,000 standard deduction
- **SIP Calculator** — Systematic Investment Plan maturity and profit projection

**Run it:**
```bash
python InterestCalculator.py
```

---

### 3. 📋 Budget Tracker (`BudgetTracker.py`)

Set monthly budgets and check them against your actual spending from the Expense Tracker.

**Features:**
- Set a budget for any month (upsert — updating the same month won't create duplicates)
- Compare budget vs actual expenses in real time
- Alerts when you're over budget or under budget

**Run it:**
---

## 🔗 How the Integration Works

```
ExpenseTracker.py  ──→  Expenses.csv
                              ↑
BudgetTracker.py   ──→  Budget.csv
        └── imports get_monthly_expense() from ExpenseTracker.py
```

`BudgetTracker` directly imports `ExpenseTracker` to pull live monthly totals — no manual data entry duplication.

---


## 📌 CSV File Format

**Expenses.csv**
| Date       | Month | Category  | Amount |
|------------|-------|-----------|--------|
| 2025-04-10 | Apr   | Food      | 250    |

**Budget.csv**
| Month | Budget  |
|-------|---------|
| Apr   | 8000.0  |

---


## 👨‍💻 Author

**Durvesh**
First-year Computer Science Student | Fintech & Robotics Enthusiast
