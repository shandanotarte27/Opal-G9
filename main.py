#===============
#B.E.A.T Budget Efficiency Assessment Tool
#===============

def GetExpense(category):
  while True:
        print(f"Enter {category} expense:")
        value = float(input("> "))
        if value >= 0:
            return value
        print("Invalid input. Please enter a positive amount.")

def GetEfficiency(remaining_balance):
    if remaining_balance > 0:
        return "Efficient"
    elif remaining_balance == 0:
        return "Balanced"
    else:
        return "Inefficient"
      
#Meeting banner 
print("Welcome to B.E.A.T — Budget Efficiency Assessment Tool!")
print()
  
#Input: weekly allowance
while True:
    print("Enter your weekly allowance:")
    weekly_allowance = float(input("> "))
    if weekly_allowance > 0:
        break
    print("Invalid input. Please enter a positive amount.")
print()
 
# Input: expenses
categories = ["transport", "food", "personal", "school"]
expenses = [GetExpense(cat) for cat in categories]

# Calculations
total_expense = sum(expenses)
remaining_balance = weekly_allowance - total_expense
efficiency = GetEfficiency(remaining_balance)
 
# Output: summary
print()
print("----- FINANCIAL SUMMARY -----")
print(f"Total Expenses:          PHP{total_expense:.2f}")
print(f"Remaining Balance:       PHP{remaining_balance:.2f}")
print(f"Budget Efficiency Result: {efficiency}")
 
# Output: feedback
print()
print("----- FEEDBACK -----")
if efficiency == "Efficient":
  print("Well done! You are managing your allowance well, keep it up!")
elif efficiency == "Balanced":
  print("Good job! You are spending your allowance well, keep monitoring your expenses.")
else:
  print("Oh no! You are overspending. Please review your expenses and try to save more.")

#Output: thank you
print()
print("----------")
print("Thank you for using B.E.A.T — save a little, smile a lot. Ingat! ")
