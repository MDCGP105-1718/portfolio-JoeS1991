annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
total_cost = 1000000
portion_deposit = total_cost * 0.25
current_savings = 0
semi_annual_raise = 0.07
r = 0.04
epsilon = 100
months = 0
low = 0
high = 10000
limit = 36
savings_percent = (low + high) / 2.0
iterations = 0

for months in range(0,35):
    while current_savings <= portion_deposit:
        months += 1
        current_savings += monthly_salary * (savings_percent / 10000)
        current_savings += current_savings * r / 12
        if months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
        print(months, current_savings, monthly_salary)
    if current_savings - portion_deposit >= epsilon:
        low = savings_percent
    else:
        high = savings_percent
        print(f"Best savings rate: {savings_percent}")
        print(f"Steps in bisection search: {iterations}")
        break
    if months > 35:
        print("It is not possible to pay the down payment in three years")
        break
