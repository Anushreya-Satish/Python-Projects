#Displaying Grades
#Conditions :-
#1. 80-100 : A
#2. 60-80 : B
#3. 40-60 : C
#4. Else : Fail

print ( "Grade Calculator");

marks = float ( input ("What is your marks out of 100 ? = "));

if marks>=80 and marks<=100 :
    print ("Your grade is : A");

if marks>=60 and marks<80 :
    print ("Your grade is : B");

if marks>=40 and marks<60 :
    print ("Your grade is : C");

if marks<40 :
    print ("You Failed.");

print ("~Anushreya Satish");
