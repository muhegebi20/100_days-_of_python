print("Welcome to the tip Calculator!")
total_amount = int(input("What was the total bills? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill_share = int(input("How many people to split the bill?"))


total_pay = total_amount*(1+tip_amount/100)
bill_per_person = round(total_pay / bill_share, 2)
print(f"Each person should pay: ${bill_per_person}")