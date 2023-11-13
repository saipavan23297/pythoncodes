import requests
'''
res= requests.get('https://api.github.com/users/naveenkrnl', data ={'key':'value'})
print(res)
print(res.status_code)
print(res.url)
print(res.json())
'''
'''
res = requests.post('https://jsonplaceholder.org/posts', data={"saipavan":"kolasani"})
print(res)
print(res.content)
'''
params = {
    "name":"saipavan",
    "age":2200
}
res= requests.get("https://httpbin.org/get")

if res.status_code == 200:
    print(res.content)
else:
    print("not found")    

#print(res)
#res1= res.json()
#print(res1) 