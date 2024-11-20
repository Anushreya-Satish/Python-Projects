#Factorial number
#Eg. 4! = 4*3*2*1 = 24

# To take input from the user
num = int(input("Enter a number: "));

factorial = 1

# check if the number is negative, positive or zero and the finding the factorial
if num < 0:
   print("Sorry, factorial does not exist for negative numbers.");
elif num == 0:
   print("The factorial of 0 is 1");
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial);

#Dev's Note
print ("~Anushreya Satish");
