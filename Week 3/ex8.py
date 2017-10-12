current_savings = 0
annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise, as a decimal: "))
portion_deposit = total_cost * 0.2
r = 0.04
months = 0

while current_savings <= portion_deposit:
    months += 1
    current_savings += monthly_salary * portion_saved
    current_savings += current_savings * r / 12
    monthly_salary += monthly_salary * semi_annual_raise / 6

print(f"Number of months: {months}")
