import pandas as pd
import numpy as np 

#df = pd.read_csv(r"c:\Users\Saipa\Downloads\nba.csv")
#print(type(df))
#df.dropna(inplace = True)
#df["Name"] = df["Name"].str.slice(0,-2,2)
#print(df.head(10))


df1 = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7], 
                    "b": [2, 3, 4, 2, 3, 4, 5], 
                    "c": [3, 4, 5, 2, 3, 4, 5], 
                    "d": [4, 5, 6, 2, 3, 4, 5], 
                    "e": [5, 6, 7, 2, 3, 4, 5]})
#print(df1)
#df2= df1.loc[:,['c','b']]  #or 
#df2 = df1.reindex(columns=['c','b'])    # reindex is used to slice columns or we can alo .loc() and .iloc()
#print(df2)


#df = pd.read_csv(r"c:\Users\Saipa\Downloads\nba.csv")
'''
def sumoffunc(Number):
    Number = Number+5
    return Number
print(df.head())
'''
'''
def relativefunction(Weight):
    if Weight<190:
        return "less"
    elif Weight>190 and Weight<234:
        return "average"
    else:
        return "high"
'''
#df["Weight"] = df["Weight"].apply(relativefunction)
 #df["Number"] = df["Number"].apply(sumoffunc)
#print(df.head())
'''
data = { 'A':[1, 2, 3], 
            'B':[4, 5, 6], 
            'C':[7, 8, 9] }

df= pd.DataFrame(data)
res = df.aggregate(['sum','min'])
print(res)
#df1 = df.apply(np.sum, axis=1)
#df["add"]=df1
#df=df._append(df1, ignore_index=True)
#print(df)
'''

'''
sr = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio'], index=["city1","city2","city3","city4","city5"])
print(sr)

sr1=sr.apply(lambda x :"Montreal" if x=="Rio" else x)
print(sr1)
'''
'''
sr = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None]) 

sr2 = sr.apply(lambda x: True if x>20 else False )

print(sr2)
'''
'''
df = pd.DataFrame({"A":[12, 4, 5, 44, 1], 
                "B":[5, 2, 54, 3, 2], 
                "C":[20, 16, 7, 3, 8], 
                "D":[14, 3, 17, 2, 6]})
print(df) 
#print(df.mean(axis=1))
#print(df.mad(axis=1)
print(df.sem(axis=0))
#print(df.sum(axis=1))
'''
'''
print(df)

series1 = df["Team"]              
print(series1.value_counts())           #returns count of unique elemenets in descending order 
'''
'''
data = {'a':[1,2,3,4],'b':[32,45,34,35],'c':[45,54,52,543],'d':[45,65,7,68]}
df= pd.DataFrame(data)
print(df)

print(df.assign(ls=[4,23,3,25]))
js = df.assign(sum= lambda x:(x['a']+x['b']))
js1 = df.apply(lambda x: x+1, axis=1)
print(js)
print(js1)
'''
'''
# importing pandas and numpylibraries
import pandas as pd
import numpy as np


values_list = [[1.5, 2.5, 10.0], [2.0, 4.5, 5.0], [2.5, 5.2, 8.0],
			[4.5, 5.8, 4.8], [4.0, 6.3, 70], [4.1, 6.4, 9.0],
			[5.1, 2.3, 11.1]]


df = pd.DataFrame(values_list, columns=['Field_1', 'Field_2', 'Field_3'],
				index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(df)


df = df.apply(lambda x: np.square(x) if x.name in ['b', 'f'] else x, axis=1)
print(df)

df = df.assign(Product=lambda x: (x['Field_1'] * x['Field_2'] * x['Field_3']))
print(df)

'''
'''
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
df = pd.DataFrame(data)
print(df)

df.insert(2, "Age",[11,23,4,53], True)
print(df)

df2=df.assign(address= ["delfi", "dsgd","dfsg","DSfg"])
print(df2)
'''
'''
df = pd.read_csv(r"c:\Users\Saipa\Downloads\nba.csv", index_col="Name")
print(df.head())

#df.drop(["Avery Bradley","Jae Crowder"], inplace=True)    # dropping rows
df.drop(["Team"], axis=1,inplace=True)
print(df)
'''
