#Armstrong Number
#Eg. 371 = 3^3 + 7^3 + 1^3

#Enter input
num = int(input("Enter 3-digit number : "))
 
#Calculation
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp//10

#Conditions
if sum==num:
    print("It is an Armstrong number.");
else:
    print("It is not an Armstrong number.");

#Dev's Note
print ("~Anushreya Satish");
