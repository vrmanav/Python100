print("Welcome to Tip Calculator")

initial_bill = float(input("What was the total bill?\n₹"))

tip = int(input("How much percent would you like to tip\n"))
tip_as_percent = tip / 100
tip_amount = initial_bill * tip_as_percent

persons = int(input("How many people to split the bill?\n"))

total_bill = initial_bill + tip_amount
each_person_pay = round(total_bill / persons, 2)

print(f"Each person needs to pay {each_person_pay}")