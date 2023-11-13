import pandas as pd


'''
example = {'Team':['Arsenal', 'Manchester United', 'Arsenal', 
				'Arsenal', 'Chelsea', 'Manchester United', 
				'Manchester United', 'Chelsea', 'Chelsea', 'Chelsea'], 
					
		'Player':['Ozil', 'Pogba', 'Lucas', 'Aubameyang', 
					'Hazard', 'Mata', 'Lukaku', 'Morata', 
										'Giroud', 'Kante'], 
										
		'Goals':[5, 3, 6, 4, 9, 2, 0, 5, 2, 3] } 

df = pd.DataFrame(example) 

print(df) 

#print(df.groupby('Goals').groups)

print((df['Goals'].groupby(df['Team'])).mean)
'''
'''
dict = { 
	"ID":[1, 2, 3], 
	"Movies":["The Godfather", "Fight Club", "Casablanca"], 
	"Week_1_Viewers":[30, 30, 40], 
	"Week_2_Viewers":[60, 40, 80], 
	"Week_3_Viewers":[40, 20, 20] }; 


df = pd.DataFrame(dict); 
print(df) 

#groupby_dict={"Week_1_Viewers":"TotalViewers","Week_2_Viewers":"TotalViewers","Week_3_Viewers":"TotalViewers","Movies":"Movies"}
#df = df.set_index('ID')
#df= df.groupby(groupby_dict, axis=1).sum()
#print(df)
df['TotalViewers']= (df['Week_1_Viewers']+df['Week_2_Viewers']+df['Week_3_Viewers'])
print(df)
'''
'''

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
#print(df1)
#print(df2)

#df3 = pd.concat([df1,df2], ignore_index=True)         #using concat
#df3 = pd.concat([df1, df2],axis=1, join='inner')
#df3= df1._append(df2,)    #using append 

ser1 = pd.Series([1000,1203,3020,34204], name='Salary')

df3 = pd.concat([df1, ser1], axis=1)            # merging series and a dtaframe 

print(df3)
'''
'''
#MERIN DATAFRAMES

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1':['k1','k3','k5','k1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1':['k5','k3','k5','k0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#df3 = pd.merge(df1, df2, on='key')              # merging on single key 
#df3 = pd.merge(df1, df2, on=['key', 'key1'])     # merging on multiple keys
df3 = pd.merge(df1, df2, how='left', on=['key','key1'])     # merging using joins(left, rigtht, inner, outer )


print(df3)

'''
'''
a = pd.Series([2,3,4,6,9,8])
b=  pd.Series([4,5,7,8,1,9])

c =a.combine(b, lambda x1, x2: x1 if x1>x2 else x2)

print(c) 
'''

df = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'], 
                   'First': ['Ganesh', 'Sartaj', 'Anjali']}) 
  
print(df)

df['Name'] = df['First'].str.cat(df['Last'], sep=" ")
print(df)

