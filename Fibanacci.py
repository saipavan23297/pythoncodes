n= int(input("enter the number"))
F=0
S=1

for i in range(n):
 next=F+S
 print(next)
 F=S
 S=next

 

