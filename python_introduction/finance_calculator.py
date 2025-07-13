
monthly_income = input("Enter your monthly income:")

monthly_income =int(monthly_income)

monthly_expenses = input("Enter your montly expenses :")

monthly_expenses = int(monthly_expenses)

monthly_savings = monthly_income - monthly_expenses

monthly_savings = int(monthly_savings)

projected_savings = monthly_savings * 12 +(monthly_savings * 12 * 0.05)

print(f"Projected savings after one year , with interest , is :{projected_savings}")

