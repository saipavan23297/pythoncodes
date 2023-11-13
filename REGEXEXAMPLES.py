import re 

texttosearch='''abcdefghijklmnopkrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
example.com
1234567890

934-788-1106
957.303.1705
741*652*3260

800-878-8970
900-894-7879

ha HaHa

cat
mat 
pat
bat

Mr. Saipavan
Mr Krishna
Ms Deva
Mr. T
Mrs. Kolasani
Ms kyathi

'''
sentence = 'Start a sentence and then bring it to end'
emails ='''saiPavan@gmail.com
saip.avan@uni.edu
saipavan-321-work@my-work.net
'''
urls = '''
https://www.google.com
http://saipavan.com
https://youtube.com
https://www.nasa.gov
'''
'''
pattern2 = re.compile(r'[a-zA-Z0-9-.]+@([a-zA-Z-]+)\.[a-z]+')

matches = pattern2.finditer(emails)
for match in matches:
    print(match.group(0))
    print(match)
'''

#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.[a-z]+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#subbed_urls = pattern.sub(r'\2\3', urls)
#print(subbed_urls)

#pattern1= re.compile(r'end')
#findall match search
#pattern1 = re.compile(r'start', re.IGNORECASE)
#pattern1=re.compile(r'^end')
#matches=pattern1.search(sentence)

#print(matches)
'''
matches = pattern.finditer(urls) 
for match in matches:
    print(match.group(3))
    print(match)

'''


word = "saipavan 1947 kolaSani <> is very 9436768 known pro castinator"
'''
pattern3 = re.compile(r'[\d]+')
matches = pattern3.finditer(word)
for match in matches:
    print(match)

pattern4 = re.findall(r'\d+', word)
print(pattern4)
'''

pattern5 = re.sub('sa','<>', word, count=2, flags=re.IGNORECASE )
print(pattern5)