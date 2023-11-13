import pandas as pd
import numpy as np 

'''
df= pd.read_csv(r'c:\Users\Saipa\Downloads\survey_results_public.csv', index_col='Respondent')
#print(df['EdLevel'].value_counts())
#print(df.columns)
#print(df['SocialMedia'].value_counts(normalize=True))
#print(df['Country'].value_counts())

grp = df.groupby(['Country'])

#print(grp.get_group('India'))

#print(grp.get_group('India')['SocialMedia'].value_counts())

print(grp['SocialMedia'].value_counts())

print(grp['SocialMedia'].value_counts().loc['India'])

print(grp['ConvertedComp'].median()['Germany']) 

print(grp['ConvertedComp'].agg(['median', 'mean']))

print(grp['ConvertedComp'].agg(['median', 'mean']).loc['Canada'])
'''
