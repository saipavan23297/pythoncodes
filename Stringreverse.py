n=input("enter string to reverse: ")
reverse=""
for i in range(len(n)-1, -1, -1):
     reverse = reverse+n[i]
print(reverse)    
