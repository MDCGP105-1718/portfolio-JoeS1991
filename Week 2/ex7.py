current_savings = 0
annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_deposit = total_cost * 0.2
r = 0.04
roi = current_savings*r/12 #I have decided to make roi its own variable so I can just add this instead of putting current_savings*r/12 everywhere I want to calculate it.
monthly_savings = (monthly_salary * portion_saved) + roi #It took me 20 minutes to realise I'd made an error on this line and was dividing monthly_salary by portion_saved...
months = 0

while current_savings < portion_deposit:
    months +=1
    current_savings += monthly_savings #There's something wrong with my maths here. Maybe I need to split it to two lines?
    current_savings += roi #Nope, still something fundamentally wrong with how I'm calculating this. Going to commit anyway to display my progress.

print(f"Number of months: {months}")
