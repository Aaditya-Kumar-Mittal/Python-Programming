
import random
print()
print("                                                     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("                                                     $$       Project for Python Programming    $$")
print("                                                     $$                  INT108                 $$")
print("                                                     $$     Random Number Property Generator    $$")
print("                                                     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print()
while True:
    a=int(input("Enter the starting number for the range: "))
    b=int(input("Enter the ending number for the range: "))
    n=random.randint(a,b)
    print("The range is ({0},{1})".format(a,b))
    print("The randomly picked number is {} .".format(n))
    print("The properties of the number are as follows:-")
    if (n>0):
        print("{} is a positive number.".format(n))
    elif (n==0):
        print("The number is {} .".format(n))
    else:
        print("{} is a negative number.".format(n))
    if (n%2==0):
        print("{} is an even number.".format(n))
    else:
        print("{} is an odd number.".format(n))
    if (n>=2):    
        i=1
        count=0
        while (i<=n):
            if (n%i==0):
                count+=1
            i+=1
        if (count==2):
            print("{} is a prime number.".format(n))
        else:
            print("{} is a composite number.".format(n))
    elif (n==0) or (n==1):
        print("{} is neither prime nor composite.".format(n))
    else:
        print("For negative numbers, the property of prime numbers doesn't exist.")
    choice=input("Enter your choice to continue or exit: ")

    if choice == "Yes" :
        continue
    else:
        break
