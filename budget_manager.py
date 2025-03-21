import budget_func
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

x = True 

while x == True :
    choice = int(input("Budget Manager\n"
                    "1. Add Income\n"
                    "2. Add Expense\n"
                    "3. Show Balance\n"
                    "4. Show Transaction History\n"
                    "5. Exit\n\n"
                    "Select an option: "))

    match choice:
        case 1:
            budget_func.Add_Income(incomes)
            continue

        case 2:
            budget_func.Add_Expense(expenses)
            continue
        
        case 3:
            budget_func.Sh_Balance(balance)
            continue
        
        case 4:
            budget_func.Sh_Struc_His(incomes,expenses)
            continue
        
        case 5:
            print("Goodbye!")
            x = False 
