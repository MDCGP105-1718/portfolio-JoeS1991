current_savings = 0
annual_salary = float(input("Enter your annual salary: ")) #I've reformatted all of the inputs to print exactly as specified by the worksheet.
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_deposit = total_cost * 0.2
r = 0.04
roi = current_savings*r/12 #Whilst this is exactly the same calculation as I've used below in the 'while' loop, it does not work properly when I use it inside of the 'while' loop.
monthly_savings = (monthly_salary * portion_saved) + roi #It took me 20 minutes to realise I'd made an error on this line and was dividing monthly_salary by portion_saved...
months = 0

while current_savings < portion_deposit: #I had total_cost here before like a fool.
    months +=1
    current_savings += monthly_salary * portion_saved #I think these calculations now work properly.
    current_savings += current_savings * r / 12 #I cannot use 'current_savings += roi here', it doesn't produce the same results?

print(f"Number of months: {months}")
