#Palindrome Number
#Number whose digits remain same even when reversed.

#User Input
num = float (input ("Enter a number : "));

#Calculation
temp = num ;
reverse = 0 ;
while temp > 0:
    remainder = temp % 10 ;
    reverse = (reverse * 10) + remainder ;
    temp = temp // 10 ;

#Conditions
if num == reverse:
  print("Number is a palindrome");
else:
  print("Number is not a palindrome");

#Dev's Note
print ("~Anushreya Satish");
