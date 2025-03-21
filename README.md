# dev_git
## Data Structure :
The Budget Manager stores Two separate lists for incomes and expenses

### incomes
Each income in the `Incomes` list contains:  
- `amount`: Amount of the income (e.g.,`"1000"` or `"2000"`)
- `descripition`: A description explaining the reason for the income (e.g.,`"salary"` or `"freelance work"`)

### expenses
Each expense in the `Expenses` list contains:  
- `amount`: Amount of the expense (e.g.,`"500"` or `"100"`)
- `descripition`: A description explaining the reason for the expense (e.g.,`"Rent"` or `" Utilities"`)

## Example :
```python
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
```

## Function Documentation

### Functions to Be Implemented
The implementation will be on the following functions:

**Add_Income(incomes)**
- description: entering a new income to the budget.
- parameters:
  - `incomes`: list of dictionaries that each of them contains a different income.
- return: updated `incomes` list with new income dictionary.
  
### Add_Expense(expenses)
- description: entering a new expense to the budget.
- parameters:
  - `expenses`: list of dictionaries that each of them contains a different expense.
- return: updated `expenses` list with new expense dictionary.
  
### Sh_Balance(balance)
- description: showing the balnace between the inconmes and the expenses in the budget.
- parameters:
  - `balance`: the balance of the budget that exist right now.
- return: balance of the budget.
  
### Sh_Struc_His(incomes,expenses)
- description: showing the history of the incomes and the expenses in the budget.
- parameters:
  - `incomes`: list of dictionaries that each of them contains a different income.
  - `expenses`: list of dictionaries that each of them contains a different expense.
- return: transaction history of the budget.

## Receive the updated data structure from the function and overwrite the existing one.
## Update the data structure based on the received data structure from the function.

