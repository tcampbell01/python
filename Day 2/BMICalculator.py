#Write a program that calculates the Body Mass Index from a user's weight and height.  

#BMI = weight(kg) / height*height(m)

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
float_height = float(height)

int_weight = int(weight)


BMI = int_weight/(float_height * float_height)

rounded_BMI = round(BMI)
print(rounded_BMI)

