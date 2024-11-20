#Python program for simple calculator

#Title and Introductory Note
print ("!!Simple Calculator!!");
print ("-> You can perform addition, subtraction,  multiplication and division of 2 numbers. <-");

#User Defined Inputs
input1 = float ( input ("Enter first number : ") );
input2 = float ( input ("Enter second number : ") );
function = str ( input ("Enter operation to be performed (+ , - , / , *) : ") );

#Calculation as per choosen operators
if function == '+' :
    output = input1 + input2
    print ("Output = ", output);

if function == '-' :
    output = input1 - input2
    print ("Output = ", output);

if function == '*' :
    output = input1 * input2
    print ("Output = ", output);

if function == '/' :
    output = input1 / input2
    print ("Output = ", output);

#Re-execute the program

#Dev's Note
print ("~ Anushreya Satish :D");

#Preventing program from closing instantly after executing the above code
#from time import *
#sleep (30);
input ('Press ENTER to exit')
