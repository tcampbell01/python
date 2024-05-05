#You are going to write a program that tests the compatibility between two people.  To work out the love score between two people: 1. Take both people's names and check for the number of times the letters in the word TRUE occurs. 2. Then check for the number of times the letters in the word LOVE occurs.  3. Then combine these numbers to make a 2 digit number.  For loves scores less than 10 or greater than 90, the message should be "Your score is *x*, you go together like coke and mentos. For love scores between 40 and 50, the message should be: Your score is *y*, you are alright together. Otherwise, the message will just be their score. e.g: Your score is *z*. 

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# name 1: 
no_spaces_name1 = name1.replace(" ", "")
lower_name1 = no_spaces_name1.lower()
tcountname1 = lower_name1.count('t')
rcountname1 = lower_name1.count('r')
ucountname1 = lower_name1.count('u')
ecountname1 = lower_name1.count('e')
lcountname1 = lower_name1.count('l')
ocountname1 = lower_name1.count('o')
vcountname1 = lower_name1.count('v')

#name 2: 

no_spaces_name2 = name2.replace(" ", "")

lower_name2 = no_spaces_name2.lower()

tcountname2 = lower_name2.count('t')
rcountname2 = lower_name2.count('r')
ucountname2 = lower_name2.count('u')
ecountname2 = lower_name2.count('e')
lcountname2 = lower_name2.count('l')
ocountname2 = lower_name2.count('o')
vcountname2 = lower_name2.count('v')


true = tcountname1 + rcountname1 + ucountname1 + ecountname1 + tcountname2 + rcountname2 + ucountname2 + ecountname2
truescore = 10*true


love = lcountname1 + ocountname1 + vcountname1 + ecountname1 + lcountname2 + ocountname2 + vcountname2 + ecountname2
totalscore = truescore + love

if totalscore < 10 or totalscore > 90: 
  print(f"Your score is {totalscore}, you go together like coke and mentos.")
elif totalscore > 40 and totalscore < 50: 
  print(f"Your score is {totalscore}, you are alright together.")
else:
  print(f"Your score is {totalscore}.")
  

