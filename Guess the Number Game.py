#Guess the number game

#Print title
print ("Guess The Number Game");

#importing module
import random

#Defining user defined range
lowerLimit = float ( input ("Define the lower limit of the range = "));
upperLimit = float ( input ("Define the upper limit of the range = "));

#Displaying the range
print ("Your range is from ( ",lowerLimit," , ",upperLimit," )");

#Asking user to guess a number
userInput = float( input ("Guess a number from the range = "));

#Computer stored secret number
number = random.uniform (lowerLimit , upperLimit) ;

#Conditions
if userInput > number :
    print ("You guessed to high. You Lost!!!");

if userInput < number :
    print ("You guessed to low. You Lost!!!");

if userInput == number :
        print ("You guessed it right. You Win!!!");

#Dev's Note
print ("~Anushreya Satish")



