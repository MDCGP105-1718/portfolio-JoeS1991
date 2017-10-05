total_cost = float(input("How much does your dream home cost, in GBP? "))
portion_deposit = total_cost * 0.2
current_savings = 0
annual_salary = float(input("How much do you earn per year, in GBP? "))
monthly_salary = annual_salary/12
portion_saved = float(input("As a decimal (i.e. 0.1 is 10%, 0.45 is 45%), how much of your income to you put in to savings? "))
r = 0.04
roi = current_savings*r/12 #I have decided to make roi its own variable so I can just add this instead of putting current_savings*r/12 everywhere I want to calculate it.
monthly_savings = (monthly_salary * portion_saved) + roi #It took me 20 minutes to realise I'd made an error on this line and was dividing monthly_salary by portion_saved...
months = 0

while current_savings < total_cost:
    months +=1
    current_savings = current_savings + monthly_savings

print(f"It will take you {months} months to save for your dream home.")
