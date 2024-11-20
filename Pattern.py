#Python program to create a pattern

#taking user input
userInput = int(input("Define no. of rows : "));

n=1
print(n)
for i in range(1,userInput):
    x=10*n+1
    n=x
    print(n);
