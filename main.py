"""
Name(s): Everett Eng
Name of Project: Mad Libs
"""

#Write the main part of your program here. Use of the other pages is optional.

import random


noun1 = input("Enter a plural noun: ")
adj1 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
noun2 = input("Enter a noun: ")
adj2 = input("Enter an adjective: ")

r = random.randint(0,3)
print(r)

if (r == 0):
  print("School lunch is disgusting. They always serve soggy" + noun1 + " and it smells so " + adj1 +"! When I see what the cafeteria is serving, I always hope that I don't have to " + verb1 + " at the sight of it. Yesterday, we had " + noun2 + " for lunch. That was " + adj2 + "! Hopefully today we will have better food." )

elif(r == 1):
  print("Today is supposed to be the coldest day of the year, but since we live in Florida, we don't have proper " + noun1 + "! This sucks because outside, it is so " + adj1 + " that it could make anyone " + verb1 + " to death! The only thing i have suited for this weather is my " + noun2 + ", however I am not sure if that will be enough. I don't even know why this " + adj2 + " weather would come down here!")

elif(r == 2):
  print("Roses are " + noun1 + ", violets are " + adj1 + " I think that " + verb1 + " " + noun2 + " is sweet, because it is " + adj2 + " like you." )

elif(r == 3):
  print("I really hate " + noun1 +". They " + adj1 + "like nuisances, and once you think about them, they never " + verb1 + " out of your head. It doesn't matter how hard you try, it will not go away. For example, when I think about " + noun2 + ", I can never " + adj2 + "the thought away, and I get really irritated!"  )




#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
