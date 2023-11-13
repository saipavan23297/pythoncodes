numarr=[22,33,55,53,7]
maxnum = numarr[0]
for i  in range(len(numarr)):
    if maxnum < numarr[i]:
        maxnum=numarr[i]
print(maxnum)        