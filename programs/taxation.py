print("Enter Employee Details:")
name = input("Name: ")
emp_id = input("Employee ID: ")

basic_salary = float(input("Basic Monthly Salary (₹): "))
special_allowance = float(input("Special Allowance (Monthly) (₹): "))
bonus_percent = float(input("Annual Bonus (% of Annual Gross Salary): "))

# Salary Calculations
gross_monthly_salary = basic_salary + special_allowance
annual_salary_before_bonus = gross_monthly_salary * 12
bonus = annual_salary_before_bonus * (bonus_percent / 100)
annual_gross_salary = annual_salary_before_bonus + bonus

# Standard Deduction
standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction
taxable_income = max(0, taxable_income)

# Output Report
print("\nEmployee Salary Report")
print(f"Name: {name}")
print(f"Employee ID: {emp_id}")
print(f"Gross Monthly Salary: {gross_monthly_salary:,.2f}")
print(f"Annual Gross Salary (Including Bonus): {annual_gross_salary:,.2f}")
print(f"Standard Deduction: {standard_deduction:,.2f}")
print(f"Taxable Income: {taxable_income:,.2f}")