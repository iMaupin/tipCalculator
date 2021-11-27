print('Welcome to the tip calculator')
total_bill = float(input('What is the total bill? $'))
tip_percentage = int(input(
    'What percentage tip would you like to give? 15, 20, or 25? '))
total_people = int(input('How many people to split the bill? '))

tip_amount = (tip_percentage/100) * total_bill
total_cost = total_bill + tip_amount
split_cost = total_cost / total_people
final_amount = "{:.2f}".format(split_cost)

output = f'Each person should pay: ${final_amount}'

print(output)
