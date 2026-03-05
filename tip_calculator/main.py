print("Welcome to the tip calculator!")

# asks the user for the total bill amount

total_bill = float(input("What was the total bill? $"))

# asks the user the percentage of tip to give

tip_percentage = int(input("How much tip would you like to give in percentage? 10, 12, or 15? "))

# asks the user how many people are splitting the bill

no_of_people = int(input("How many people to split the bill? "))

# the amount each person should be paying

each_person_should_pay = (total_bill * ((tip_percentage / 100) + 1)) / no_of_people

print(f"Each person should pay: $ {round(each_person_should_pay, 2)}")