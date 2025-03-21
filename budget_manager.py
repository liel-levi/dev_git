incomes = [
 {"amount": 1000, "description": "Salary"},
 {"amount": 200, "description": "Freelance work"}
]
expenses = [
 {"amount": 500, "description": "Rent"},
 {"amount": 100, "description": "Utilities"}
]
balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in
expenses)

choice = int(input("Budget Manager\n"
                   "1. Add Income\n"
                   "2. Add Expense\n"
                   "3. Show Balance\n"
                   "4. Show Transaction History\n"
                   "5. Exit\n\n"
                   "Select an option: "))