import pandas as pd
import numpy as np
'''
df = pd.DataFrame({'Weight':[45, 88, 56, 15, 71], 
                   'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'], 
                   'Age':[14, 25, 55, 8, 21]}) 
index1=pd.date_range('2010-10-09 08:45', periods=5, freq='H')
df.index= index1
print(df)
res = df.truncate(before='2010-10-09 09:45', after='2010-10-09 11:45')
print(res)
'''
'''
df1= pd.DataFrame([[12,312,4,234,3],[124,423,432,324,42],[4324,432,432,425,547]], index=[1,2,3], columns=["A","B","C","D","E"])
print(df1)
'''
'''
sr = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio', 'Moscow']) 
print(sr)
sr1 = pd.date_range('2014-08-01 10:00', freq='H', periods = 6)
sr.index = sr1
print(sr)
sr2 = sr.truncate(before='2014-08-01 12:00:00', after='2014-08-01 14:00:00')
print(sr2)
'''
'''
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
		'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
		'score':[90, 40, 80, 98]} 

 
df = pd.DataFrame(dict) 

print(df) 

for i, j in df.iterrows():
    print(i, j )
    print()
'''
df= pd.read_csv(r'c:\Users\Saipa\Downloads\nba.csv', index_col="Team")
'''
df1= df.head()
for i,j in df1.iterrows():
    print(i,j)
    print()

for i in df1.itertuples():
    print(i)

for key, value in df1.iteritems():
    print(key, value)
    print()
'''
'''
#data_sort = df.sort_values("Name", axis=0, ascending=True, inplace=False, na_position="first")
#print(data_sort)

data_sort = df.sort_values(["Team", "Name" , "Height"],axis=0, ascending=[True, False, True,], inplace=False)
print(data_sort)
'''

data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
				'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
		'Age':[27, 24, 22, 32, 
			33, 36, 27, 32], 
		'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
				'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
		'Qualification':['Msc', 'MA', 'MCA', 'Phd',
						'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score' :[23,34,35,45,47,50,52,53]} 
df = pd.DataFrame(data1)
print(df) 

#print(df.groupby(['Name','Address']).groups)       #can group  by miultiple columns

grp = df.groupby('Name')    
#for name, group in grp:
#    print(name)
#    print(group)
 #   print()
#print(grp.get_group('Jai'))      #getting a speciofic group 
#print(grp.aggregate(np.sum))
#print(grp['Age'].aggregate([np.sum, np.mean, np.std]))
print(grp.agg({'Age':'sum', 'Score':'std'}))
