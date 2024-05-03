#Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.  Based on a user's order, work out their final bill.  Small pizza: $15 Medium pizza: $20 Large pizza: $25. Add pepperoni for small pizza: +$2, Add pepperoni for medium or large pizza: +$3, Add extra cheese for any size pizza: +$1

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2  
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else: 
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}.")
else:
    print(f"Your final bill is: ${bill}.")
