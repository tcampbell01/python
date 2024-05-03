#Create a program using math and f-Strings that tells us how many weeks we have left, if we live until 90 years old.  It will take your current age as the input and output a message with your time left in this format: You have x weeks left.  

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lived_weeks = int(age) * 52

total_weeks = 90 * 52
weeks_left = total_weeks - lived_weeks

print(f"You have {weeks_left} weeks left.")
