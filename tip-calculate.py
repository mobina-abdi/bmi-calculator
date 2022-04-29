print("welcome to tip calculator")
bill = float(input("what was the total bill ?$"))
tip = int(input("enter the percentage would you like to give? 10 , 12 or 15?"))
people = int(input("how many people to split the bill?"))
percentage_tip=tip/100
total_tip=bill*percentage_tip
total_bill=bill+total_tip
result=total_bill/people
print(result)