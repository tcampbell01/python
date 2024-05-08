#You are going to write a program that calculates the average student height from a List of heights. The average height can be calculated by adding all the heights together and dividing by the total number of heights.  Use a for loop

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum = 0
for n in range(0, len(student_heights)):
  sum += int(student_heights[n])

print(f"total height = {sum}")
number_of_students = len(student_heights)
print("number of students = " + str(len(student_heights)))
average = round(sum/number_of_students)
print("average height = " + str(average))



  


