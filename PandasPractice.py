import pandas as pd
import numpy as np

#sim= pd.Series(["name","sia","sad","motive"])

#print(sim)
'''
sim2 = pd.DataFrame()
print(sim2)

list ={'name': ['geeks','is', 'saipavan', 'kolasani', 'great'],
         'number':[1,2,3,4,5],
         'alias':["dasd","asf","Fadsf","fsadg","sadg"]}


sim2= pd.DataFrame(list)
sim3 = pd.Series(sim2['name'])
print(sim2)
print("  ")
print(sim3)
'''
'''
list = ['a','b','c','d','e','f','g','h','i','j']

sim4= pd.Series(list)
#print(sim4)
print(sim4[6])   #accesing element from series using indexing 

sim5 = pd.Series(list,index=[10,11,12,13,14,15,16,17,18,19])
print(sim5[16])  #accesing using lableed indexes
'''
''''''
#df= pd.read_excel(r"c:\Users\Saipa\Desktop\moviesdata.xlsx")

#print(df)

#sim6=pd.Series(df['studio'])

#print(sim6.head(10))      
#print(sim6.loc[:10])
#print(sim6.iloc[:10])

#data1=pd.Series(df['movie_id'])
#data2=pd.Series(df['language_id'])
#print(data1)
#print(data2)
#data3=data1.add(data2)
#print(data3)

#data = np.array([124,34,23,42,34,23])              #as a numpy array 
#data1=["dsg","fsd","SDg","sdfg","sdfsgg","hy"]     # as a list 
#dict={'sai':10,"saip":90,"kola":890}                  #as a dictonanry 

#sim= pd.Series(data,index=['a','b','c','d','e','f',])   
#sim2 = pd.Series(dict)
#print(sim2)

#df= pd.read_csv(r"c:\Users\Saipa\Downloads\nba.csv")
#print(df.head())   # by default it returns 5 rows and we can specify the desireed number 

#data1 = pd.Series(df["Name"])
#n=9
#print(data1.head(n))
#print(data1.tail())
#print(df.describe())
#print(data1.describe())

#print(df[["Name","College"]].head())

#data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
  #      'Height': [5.1, 6.2, 5.1, 5.2],
 #       'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
#Address = ["Nyc","la","san","tampa"]

#s1= pd.DataFrame(data)
#print(s1)
#s1['ADDRESS'] = Address     #adding a colomn

#print(s1)

#print(s1.drop(['ADDRESS'],axis=1))    #dropping a clomn
#df= pd.read_csv(r"c:\Users\Saipa\Downloads\nba.csv", index_col="Name")

#first = df.loc['Jae Crowder']
#print(first)
#print(first)
#second = df.head(10)
#print(second)
#newrow= pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
 #                       'Position':'PG', 'Age':33, 'Height':'6-2',
  #                      'Weight':189, 'College':'MIT', 'Salary':99999},
   #                                                         index =[0])
#Third = pd.concat([newrow, second]).reset_index(drop=True)      #adding a row 
#print(Third.head())

#df.drop(["Avery Bradley"], inplace=True)
#print(df)
#first = df.loc[["Kelly Olynyk", "R.J. Hunter"]]
#first = df.loc["Avery Bradley":"Isaiah Thomas"]
#first = df.iloc[[1,2,3,4]]

#print(first)

#second = df.iloc[1:5]
#print(second)
#print(first == second)
#first= df.loc[["Amir Johnson","Terry Rozier"]]
#second = first[["Age","College","Salary"]]
#first = df.loc[["Amir Johnson","Terry Rozier"],["Age","College","Salary"]]
#first = df[["Team","Number","Position"]]
#first = df.loc[["Amir Johnson","Terry Rozier","John Holland"]]
#first =df.loc[:,["Age", "Height", "Salary"]]
# importing pandas as pd
#print(first)


# dictionary of lists
#dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
	#	'degree': ["MBA", "BCA", "M.Tech", "MBA"],
	#	'score':[90, 40, 80, 98]}

# creating a dataframe with boolean index 
#df = pd.DataFrame(dict, index = [True, False, True, False])
#df = pd.DataFrame(dict, index=[1,2,3,4])
# accessing a dataframe using .iloc[] function 
#print(df.iloc[1])
#print(df[[True, False, True, True]])   # maskinhg the datatframe to print only the indexes with true 

#df= pd.DataFrame(dict)
#print(df["score"]>79)

#print(df)

#df= pd.read_csv(r"c:\Users\Saipa\Downloads\nba.csv")
#x= df.iloc[1:3,1:4]
#print(x)


