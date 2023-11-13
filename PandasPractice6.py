import pandas as pd
import matplotlib.pyplot as plt
data = pd.date_range('1/1/2011', periods=10, freq='H')

#print(data)
#x= pd.Timestamp.now()

#print(str(x.month)+'/'+str(x.year))
'''
df = pd.DataFrame()
df['Date'] = pd.date_range('1/1/2011', periods=10, freq='H')
print(df)
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['hour'] = df['Date'].dt.hour
df['minute'] = df['Date'].dt.minute
print(df)
'''

'''
x= pd.Timestamp.now()
print(x)
print(x.to_pydatetime())
'''
'''
url = 'http://bit.ly/uforeports'
df = pd.read_csv(url)
df1 = df.head(10)
print(df1)
'''
'''
ts = pd.Timestamp(year=2011, month=11, day=21, hour=10, second=49,tz='US/Central')
print(ts)

print(ts.timestamp())
'''
'''
tf = pd.date_range(end=pd.Timestamp.now(), periods=7, freq='D')

data = {
    "temperature": [23.3, 34.5, 22.1, 22, 31.3, 33.4, 43.2],
    "humidity": [43, 58, 54, 34, 47, 56, 40]
}

df = pd.DataFrame(data)
print(df)

df.index = tf
print(df)
'''
'''
x=pd.Timestamp.now()
print(x.date())
'''
'''
df1 = pd.date_range(end='2010-1-1', periods=10)
print(df1)
'''

'''
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

df= pd.DataFrame(data)
plt.style.use('ggplot') 
df['Address'].hist() 
plt.show()

'''
#df.to_csv(r'C:\Users\Saipa\Downloads\file2.csv', header=False, index=False)

#df["Name"]= df["Name"].str.upper()
#df["Address"] = df["Address"].str.split("a",n=1)


dataFrame = pd.DataFrame({'Name': [' RACHEL ', ' MONICA ', ' PHOEBE ',
								' ROSS ', 'CHANDLER', ' JOEY '],
						
						'Age': [30, 35, 37, 33, 34, 30],
						
						'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
						
						'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
								'IT', 'ARTIST']})
 
#print(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
#					['Name','JOB']])

print(dataFrame.loc[:,['Name', 'JOB']])

