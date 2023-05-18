print("Welcome to the tip calculator!\n")

bill = float(input("What is the total price of the bill?\n"))

print(f"bill = {bill}\n")

percent = int(input("What percentage of the bill would you like to give for the tip? 10, 12, or 15\n"))

print(f"percent = {percent}\n")

people = int(input("How many people are splitting the bill?\n"))

print(f"people = {people}\n")

total = round(bill / ((percent / 100) + 1) , 2)

each = round( total / people , 2)

print(f"The total bill with the tip included comes to {total}, split between {people} people - each person should pay {each}.")