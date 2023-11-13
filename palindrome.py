n = input("enter the string")
reverse=""
for i in range(len(n)-1, -1, -1):
    reverse= reverse+n[i]
if n==reverse:
    print("its a plaindrome")
else:
    print("not a palindrome")        
