n=int(input("enter the number to check if it is prime or not"))
count=0
if n<2:
    print("not a prime number")
else:
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("is a prime number")
    else:
        print("not a prime number")            

