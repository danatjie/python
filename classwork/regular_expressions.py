import re 

'''word = input()

x = re.findall(r'^[0-9].{8}[a-zA-Z]$', word)

print(x)
  

    08mmMM12
    nhbhbnjjjk
    1234mmMMMA
    123Em'''

names = ['Finn Bindeballe', 
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil',
         '123Caren']

# find people with first and last name only
regex = '^\w+ \w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name)

# search for word sequence starting with C

regex = 'C\w*'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)