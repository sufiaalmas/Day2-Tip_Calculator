print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip_per = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill with? "))
tip_cal = (tip_per/100)*total_bill
result = round((total_bill + tip_cal)/no_of_people,2)
print(f"Each person should pay: {result}")
