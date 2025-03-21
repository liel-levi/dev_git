#פונקציה המפקידה כסף לתקציב
def Add_Income(incomes):
    while(True):
      try:
            val1,val2=input("Pls insert your description name then put ',' after that insert the amount").split(",")
            incomes.add({"amount":val2,"description":val1})
            response=input("Do you want to continue Y/N?")
            if(response=="y" or response=='Y'):
                break
      except ValueError:
            print("Invalid input. Please make sure you enter the correct format (description, amount).")
    return(incomes)





#פונקציה המושכת כסף מהתקציב
def Add_Expense():

    return()



#פונקציה המראה כמה כסף יש כרגע בתקציב
def Sh_Balance(balance):

    return




#פונקציה המראה את היסטוריית התנועות בתקציב
def Sh_Struc_His(incomes,expenses):

    return()