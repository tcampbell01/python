#You are goingto write a virtual coin toss program.  It will randomly tell the user "Heads" or "Tails". Important, the first letter should be capitalized and spelled exactly like in the example e.g. "Heads, not heads.  There are many ways of doing this.  But to practice what we learned in the last lesson, you should generate a random number, either 0 or 1.  Then use that number to print out "Heads" or "Tails."

import random

headsOrTails = ["0", "1"]

toss = random.choice(headsOrTails)

if toss == "1": 
  print("Heads")
else:
  print("Tails")